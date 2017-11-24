import unittest
from Helpers.GetConfig import GetConfig
from Helpers.GetMachines import GetAWSConfig



class BaseTest(unittest.TestCase):

    # AWS_ACCESS = GetConfig('AWS_ACCESS_KEY')
    # AWS_SECRET = GetConfig('AWS_SECRET_KEY')

    # HUB_MACHINE = GetAWSConfig('HUB_MACHINE_IP')
    # LOCAL_APPIUM_URL = GetConfig('LOCAL_APPIUM_URL')?

    def setUp(self):
        super().setUp()