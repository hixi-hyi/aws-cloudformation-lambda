from unittest import TestCase
import cfntest
from src.index import Strings

def get(c, name):
  return c.response.get_data(name)

class Test(TestCase):
  def test_one_case(self):
    context = cfntest.get_context()
    event = cfntest.get_create_event({"Values": ["dEv"]})

    c = Strings(event, context)
    c.run()

    self.assertEqual(get(c, "Upper"), "DEV")
    self.assertEqual(get(c, "Lower"), "dev")
    self.assertEqual(get(c, "Camelize"), "Dev")
    self.assertEqual(get(c, "CamelizeLower"), "dev")
    self.assertEqual(get(c, "Dasherize"), "dEv")
    self.assertEqual(get(c, "DasherizeLower"), "dev")
    self.assertEqual(get(c, "DasherizeUpper"), "DEV")
    self.assertEqual(get(c, "Snakelize"), "dEv")
    self.assertEqual(get(c, "SnakelizeLower"), "dev")
    self.assertEqual(get(c, "SnakelizeUpper"), "DEV")
    self.assertEqual(get(c, "Titlize"), "Dev")
    self.assertEqual(get(c, "Dotize"), "dEv")
    self.assertEqual(get(c, "DotizeLower"), "dev")
    self.assertEqual(get(c, "DotizeUpper"), "DEV")

  def test_simple_two_case(self):
    context = cfntest.get_context()
    event = cfntest.get_create_event({"Values": ["dev", "hixi"]})

    c = Strings(event, context)
    c.run()

    self.assertEqual(get(c, "Upper"), "DEVHIXI")
    self.assertEqual(get(c, "Lower"), "devhixi")
    self.assertEqual(get(c, "Camelize"), "DevHixi")
    self.assertEqual(get(c, "CamelizeLower"), "devHixi")
    self.assertEqual(get(c, "Dasherize"), "dev-hixi")
    self.assertEqual(get(c, "DasherizeLower"), "dev-hixi")
    self.assertEqual(get(c, "DasherizeUpper"), "DEV-HIXI")
    self.assertEqual(get(c, "Snakelize"), "dev_hixi")
    self.assertEqual(get(c, "SnakelizeLower"), "dev_hixi")
    self.assertEqual(get(c, "SnakelizeUpper"), "DEV_HIXI")
    self.assertEqual(get(c, "Titlize"), "Dev Hixi")
    self.assertEqual(get(c, "Dotize"), "dev.hixi")
    self.assertEqual(get(c, "DotizeLower"), "dev.hixi")
    self.assertEqual(get(c, "DotizeUpper"), "DEV.HIXI")

  def test_complex_two_case(self):
    context = cfntest.get_context()
    event = cfntest.get_create_event({"Values": ["dEv", "hIxi"]})

    c = Strings(event, context)
    c.run()

    self.assertEqual(get(c, "Upper"), "DEVHIXI")
    self.assertEqual(get(c, "Lower"), "devhixi")
    self.assertEqual(get(c, "Camelize"), "DevHixi")
    self.assertEqual(get(c, "CamelizeLower"), "devHixi")
    self.assertEqual(get(c, "Dasherize"), "dEv-hIxi")
    self.assertEqual(get(c, "DasherizeLower"), "dev-hixi")
    self.assertEqual(get(c, "DasherizeUpper"), "DEV-HIXI")
    self.assertEqual(get(c, "Snakelize"), "dEv_hIxi")
    self.assertEqual(get(c, "SnakelizeLower"), "dev_hixi")
    self.assertEqual(get(c, "SnakelizeUpper"), "DEV_HIXI")
    self.assertEqual(get(c, "Titlize"), "Dev Hixi")
    self.assertEqual(get(c, "Dotize"), "dEv.hIxi")
    self.assertEqual(get(c, "DotizeLower"), "dev.hixi")
    self.assertEqual(get(c, "DotizeUpper"), "DEV.HIXI")

  def test_complex_three_case(self):
    context = cfntest.get_context()
    event = cfntest.get_create_event({"Values": ["dEv", "hIxi", "tEmp"]})

    c = Strings(event, context)
    c.run()

    self.assertEqual(get(c, "Upper"), "DEVHIXITEMP")
    self.assertEqual(get(c, "Lower"), "devhixitemp")
    self.assertEqual(get(c, "Camelize"), "DevHixiTemp")
    self.assertEqual(get(c, "CamelizeLower"), "devHixiTemp")
    self.assertEqual(get(c, "Dasherize"), "dEv-hIxi-tEmp")
    self.assertEqual(get(c, "DasherizeLower"), "dev-hixi-temp")
    self.assertEqual(get(c, "DasherizeUpper"), "DEV-HIXI-TEMP")
    self.assertEqual(get(c, "Snakelize"), "dEv_hIxi_tEmp")
    self.assertEqual(get(c, "SnakelizeLower"), "dev_hixi_temp")
    self.assertEqual(get(c, "SnakelizeUpper"), "DEV_HIXI_TEMP")
    self.assertEqual(get(c, "Titlize"), "Dev Hixi Temp")
    self.assertEqual(get(c, "Dotize"), "dEv.hIxi.tEmp")
    self.assertEqual(get(c, "DotizeLower"), "dev.hixi.temp")
    self.assertEqual(get(c, "DotizeUpper"), "DEV.HIXI.TEMP")

