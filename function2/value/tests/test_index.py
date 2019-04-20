from unittest import TestCase
import cfntest
from src.index import Value

class TestScenario(TestCase):

  def test_default(self):
    context = cfntest.get_context()
    create_event = cfntest.get_create_event({"Value": "AAA"})
    update_event = cfntest.get_update_event({"Value": "BBB"}, cfntest.get_properties(create_event))
    delete_event = cfntest.get_delete_event(cfntest.get_properties(update_event), cfntest.get_properties(update_event))

    physical_resource_id = ''
    if True:
      c = Value(create_event, context)
      c.run()
      self.assertEqual(c.response.get_data("Value"), "AAA")
      self.assertEqual(c.response.physical_resource_id, "AAA")

    if True:
      c = Value(update_event, context)
      c.run()
      self.assertEqual(c.response.get_data("Value"), "BBB")
      self.assertEqual(c.response.physical_resource_id, "BBB")



