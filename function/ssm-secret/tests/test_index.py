from unittest import TestCase
from unittest.mock import MagicMock
from src.index import Secret
import cfntest

class TestCreate(TestCase):
  def default(self):
    request = cfntest.get_create_event({"Name": "/test/demo"})
    c = Secret(request, cfntest.get_context())

    Secret.get_ssm = MagicMock()
    Secret.get_ssm.return_value = ""



