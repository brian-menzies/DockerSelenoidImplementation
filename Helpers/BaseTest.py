import os
from bs4 import BeautifulSoup
from Helpers.FilePath import get_full_path
os.environ['PROJECTFOLDER'] = get_full_path('')
from sauceclient import SauceClient
from selenium import webdriver as seleniumWebdriver
from selenium.webdriver import DesiredCapabilities
from time import sleep, time
import unittest
import sys
import builtins
import threading
from appium import webdriver
from appium_selector.DeviceSelector import DeviceSelector
from boto.ec2.connection import EC2Connection

def GetConfig(configName):
    if 'PROJECTFOLDER' in os.environ:
        configPath = os.environ.get('PROJECTFOLDER')
        if configPath[-1] == '/':
            configPath = configPath[:-1]
    else:
        raise EnvironmentError('No PROJECTFOLDER environment variable set.  Can not find Config.xml')

    if configName.lower() == 'projectfolder':
        return configPath

    if os.path.exists(configPath):
        config = open(configPath + '/Config.xml', 'r')
    else:
        config = open(configPath + '/Config.xml', 'w')

    soup = BeautifulSoup(config, 'xml')
    node = soup.find(configName)
    config.close()
    if node==None:
        raise ValueError("Could not find value in Config.XML for [%s]" % configName)
    return node.text


class BaseTest(unittest.TestCase):

    AWS_ACCESS = GetConfig('AWS_ACCESS_KEY')
    AWS_SECRET = GetConfig('AWS_SECRET_KEY')

    GRID_URL = GetConfig('GRID_URL') + '/wd/hub'
    LOCAL_APPIUM_URL = GetConfig('LOCAL_APPIUM_URL')

    def setUp(self):
        super().setUp()

        ec2conn = EC2Connection(self.AWS_ACCESS, self.AWS_SECRET)
        reservations = ec2conn.get_all_instances()
        hosts = [i.public_dns_name + ":8080" for r in reservations
                 for i in r.instances if (i.state == u'running' and i.key_name == u'selenoidmachine')
