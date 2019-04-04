from unittest import TestCase
from unittest.mock import MagicMock, patch
from moto import mock_ssm
from src.index import Secret
import cfntest
import boto3

def get_ssm(name):
  ssm = boto3.client('ssm')
  return ssm.get_parameter(Name=name, WithDecryption=True)['Parameter']['Value']


class TestCreate(TestCase):
  @mock_ssm
  def test_default(self):
    request = cfntest.get_create_event({"Name": "/test/demo"})
    c = Secret(request, cfntest.get_context())
    c.run()
    self.assertEqual(get_ssm("/test/demo"), c.response.get_data("Secret"))


class TestScenario(TestCase):
  @mock_ssm
  def test_default(self):
    context = cfntest.get_context()
    create_event = cfntest.get_create_event({"Name": "/test/demo"})
    update_event = cfntest.get_update_event({"Name": "/test/demo", "Length": "12"}, cfntest.get_properties(create_event))
    delete_event = cfntest.get_delete_event(cfntest.get_properties(update_event), cfntest.get_old_properties(update_event))

    if True:
      c = Secret(create_event, context)
      c.run()
      self.assertEqual(get_ssm("/test/demo"), c.response.get_data("Secret"))
      self.assertEqual(len(get_ssm("/test/demo")), 32)

    if True:
      c = Secret(update_event, context)
      c.run()
      self.assertEqual(len(get_ssm("/test/demo")), 12)

    if True:
      c = Secret(delete_event, context)
      c.run()
      with self.assertRaises(Exception):
        get_ssm("/test/demo")
