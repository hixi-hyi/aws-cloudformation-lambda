from cfnprovider import CustomResourceProvider, get_logger
import os
logger = get_logger(__name__)
env = os.environ

class Value(CustomResourceProvider):
  def init(self):
    self._value = self.get('Value')

    self.response.physical_resource_id = self.id
    self.response.set_data('Value', self._value)

  @property
  def id(self):
    return "{}".format(self._value)

  def create(self, policies):
    pass

  def update(self, policies):
    pass

  def delete(self, policies):
    pass

def handler(event, context):
  c = Value(event, context)
  c.handle()
