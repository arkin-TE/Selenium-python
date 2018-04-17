# -*- coding: utf-8 -*-
import os
import unittest
from selenium.webdriver.support.wait import WebDriverWait
from lib.base.browsercap import BrowserEngine
from lib.base.logger import Logger
from lib.common.ConfigParser import SafeConfigParser

pwd = os.getcwd()

logger = Logger(logger="Base").getlog()
class Base(unittest.TestCase):

    def setUp(self):
        parser = SafeConfigParser()
        file_path =  os.path.abspath(os.path.dirname(pwd) + os.path.sep + "..") + '\\config.ini'
        parser.read(file_path)

        self.browser = BrowserEngine(self)

    def login(self):

        self.driver = self.browser.open_browser(self)

