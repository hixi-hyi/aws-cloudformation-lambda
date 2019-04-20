from cfnprovider import CustomResourceProvider, get_logger
import os
logger = get_logger(__name__)
env = os.environ

class Debug(CustomResourceProvider):
  def init(self):
    print("env", env)
    print("request", self._request)
    print("context", self._context)

  def create(self, policies):
    pass

  def update(self, policies):
    pass

  def delete(self, policies):
    pass

def handler(event, context):
  c = Debug(event, context)
  c.handle()
