from botocore.vendored import requests
import json
import traceback
from logging import getLogger, DEBUG, StreamHandler, Formatter
log_handler = StreamHandler()
log_handler.setLevel(DEBUG)
logger = getLogger(__name__)
logger.setLevel(DEBUG)
logger.addHandler(log_handler)
formatter = Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log_handler.setFormatter(formatter)

def get_logger(name):
  return logger.getChild(name)

def policy(name):
  if name:
    return Policy(name)
  return Policy([])

class Policies(object):
  def __init__(self, policies):
    self.policies = policies
  def has(self, name):
    return name in self.policies

class Response(object):
  def __init__(self, request):
    self.response = {
        'Status': "SUCCESS",
        'Reason': '',
        'PhysicalResourceId': request.get('PhysicalResourceId', 'initial value'),
        'StackId': request['StackId'],
        'RequestId': request['RequestId'],
        'LogicalResourceId': request['LogicalResourceId'],
        'NoEcho': False,
        'Data': {},
    }
  @property
  def physical_resource_id(self):
    return self.response['PhysicalResourceId']
  @physical_resource_id.setter
  def physical_resource_id(self, value):
    self.response['PhysicalResourceId'] = value
  @property
  def status(self):
    return self.response['Status']
  @status.setter
  def status(self, value):
    self.response['Status'] = value
  @property
  def reason(self):
    return self.response['Reason']
  @reason.setter
  def reason(self, value):
    self.response['Reason'] = value

  def set_data(self, key, value):
    self.response['Data'][key] = value
  def get_data(self, key):
    return self.response['Data'][key]
  def to_json(self):
    return json.dumps(self.response)

class CustomResourceProvider(object):
  def __init__(self, request, context):
    self._context = context
    self._request = request
    self._response = Response(request)
    self.init()
  @property
  def properties(self):
    return self._request['ResourceProperties']
  @property
  def old_properties(self):
    return self._request['OldResourceProperties']
  @property
  def request_type(self):
    return self._request['RequestType']
  @property
  def response(self):
    return self._response
  @response.setter
  def response(self, value):
    self._response = value

  def get_policies(self, request_type, default):
    return self.get('Policies', {}).get(request_type, default)
  def get(self, name, default=None):
    return self.properties.get(name, default)
  def get_old(self, name, default=None):
    return self.old_properties.get(name, default)

  def send_response(self):
    url = self._request['ResponseURL']
    data = self.response.to_json()
    headers = {
      'content-type' : '',
      'content-length' : str(len(data))
    }
    logger.debug("Response body:%s", data)
    logger.debug("[Restoration Url] curl '%s' -X PUT -H 'Content-Type: ' --data '%s'", url, data)
    try:
      response = requests.put(url, data=data, headers=headers, timeout=5)
      logger.debug("Status code: %s", response.reason)
    except Exception as e:
      logger.debug("send(..) failed execution requests.out(..): %s", str(e))

  def failed(self, reason):
    self.response.status = 'FAILED'
    self.response.reason = reason
    logger.info("failed the function: %s", reason)

  def init(self):
    self.failed("The method init of %s must be override a subclass method." %self)

  def create(self, policies):
    self.failed("The method create of %s must be override a superclass method." % self)
  def default_creation_policies(self):
    return []

  def update(self, policies):
    self.failed("The method update of %s must be override a superclass method." % self)
  def default_update_policies(self):
    return []

  def delete(self, policies):
    self.failed("The method delete of %s must be override a superclass method." % self)
  def default_deletion_policies(self):
    return []

  def run(self):
    if self.request_type == 'Create':
      policies = Policies(self.get_policies('Creation', self.default_creation_policies()))
      self.create(policies)
    elif self.request_type == 'Update':
      policies = Policies(self.get_policies('Update', self.default_update_policies()))
      self.update(policies)
    elif self.request_type == 'Delete':
      policies = Policies(self.get_policies('Deletion', self.default_deletion_policies()))
      self.delete(policies)
    else:
      raise

  def handle(self):
    try:
      self.run()
    except Exception as e:
      logger.critical(traceback.format_exc())
      self.failed(str(e))
    finally:
      self.send_response()

