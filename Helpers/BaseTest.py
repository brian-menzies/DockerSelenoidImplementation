import unittest
from Helpers.GetConfig import GetConfig
from Helpers.GetAWSConfig import GetAWSConfig



class BaseTest(unittest.TestCase):

    AWS_ACCESS = GetAWSConfig('AWS_ACCESS_KEY')
    AWS_SECRET = GetAWSConfig('AWS_SECRET_KEY')

    AWS_GRID_MACHINE = GetAWSConfig('HUB_MACHINE_IP')
    LOCAL_APPIUM_URL = GetConfig('LOCAL_APPIUM_URL')

    def setUp(self):
        super().setUp()