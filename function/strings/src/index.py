from cfnprovider import CustomResourceProvider, get_logger
from copy import copy
import string
logger = get_logger(__name__)

class Strings(CustomResourceProvider):
  def init(self):
    self._values = self.get('Values')

    self.response.physical_resource_id = self.id

  @property
  def id(self):
    return "{}".format('.'.join(self._values))

  @property
  def values(self):
    return copy(self._values)

  def upper(self):
    return ''.join(s.upper() for s in self.values)

  def lower(self):
    return ''.join(s.lower() for s in self.values)

  def camelize(self):
    return ''.join(s.capitalize() for s in self.values)

  def camelize_lower(self):
    strings = self.values
    ret = strings.pop(0).lower()
    return ret + ''.join(s.capitalize() for s in strings)

  def dasherize(self):
    return '-'.join(s for s in self.values)
  def dasherize_lower(self):
    return '-'.join(s.lower() for s in self.values)
  def dasherize_upper(self):
    return '-'.join(s.upper() for s in self.values)

  def snakelize(self):
    return '_'.join(self.values)
  def snakelize_lower(self):
    return '_'.join(s.lower() for s in self.values)
  def snakelize_upper(self):
    return '_'.join(s.upper() for s in self.values)

  def dotize(self):
    return '.'.join(self.values)
  def dotize_lower(self):
    return '.'.join(s.lower() for s in self.values)
  def dotize_upper(self):
    return '.'.join(s.upper() for s in self.values)

  def titlize(self):
    return ' '.join(self.values).title()

  def run(self):
    self.response.set_data('Upper', self.upper())
    self.response.set_data('Lower', self.lower())
    self.response.set_data('Camelize', self.camelize())
    self.response.set_data('CamelizeLower', self.camelize_lower())
    self.response.set_data('Dasherize', self.dasherize())
    self.response.set_data('DasherizeLower', self.dasherize_lower())
    self.response.set_data('DasherizeUpper', self.dasherize_upper())
    self.response.set_data('Snakelize', self.snakelize())
    self.response.set_data('SnakelizeLower', self.snakelize_lower())
    self.response.set_data('SnakelizeUpper', self.snakelize_upper())
    self.response.set_data('Dotize', self.dotize())
    self.response.set_data('DotizeLower', self.dotize_lower())
    self.response.set_data('DotizeUpper', self.dotize_upper())
    self.response.set_data('Titlize', self.titlize())

  def create(self, policies):
    self.run()

  def update(self, policies):
    self.run()

  def delete(self, policies):
    pass

def handler(event, context):
  c = Strings(event, context)
  c.handle()
