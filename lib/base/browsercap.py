# -*- coding: utf-8 -*-
import os.path

from selenium import webdriver

from lib.base.logger import Logger
from lib.common import ConfigParser

logger = Logger(logger="BrowserEngine").getlog()

pwd = os.getcwd()
class BrowserEngine(object):

    dir = os.path.dirname(os.path.abspath('.'))
    chrome_driver = dir + '/common/chromedriver.exe'

    def __init__(self,driver):
        self.driver = driver


    def open_browser(self,driver):
        """
        Select the browser to open.

        """
        config = ConfigParser.ConfigParser()
        file_path = os.getcwd() + '\\config.ini'

        config.read(file_path)

        browser = config.get("browser","browserName")
        logger.info("You had select %s browser" % browser)
        url = config.get("webServer","URL")
        logger.info("The test server url is: %s" % url)




        if browser == 'Firefox':
            driver = webdriver.Firefox()
            logger.info("Staring firefox browser.")
        elif browser == 'Chrome':
            driver = webdriver.Chrome()
            logger.info("Staring Chrome browser.")
        elif browser== "IE":
            driver = webdriver.Ie()
            logger.info("Staring IE browser.")
        # elif browser =='node':
        #     chrome_capabilities = {
        #         "browserName": "chrome",
        #         "version": "",
        #         "platform": "ANY",
        #         "javascriptEnabled": True,
        #         # "marionette": True,
        #     }
        #     driver = webdriver.Remote("http://192.168.99.100:5555/wd/hub",desired_capabilities=chrome_capabilities)
        #     logger.info("Staring node-chrome")

        driver.get(url)
        logger.info("Open url: %s" % url)
        driver.maximize_window()
        logger.info("Maximize the current window.")
        driver.implicitly_wait(30)
        logger.info("Set imlicitly wait 30 seconds.")
        return  driver

    def quit_browser(self):
        logger.info("Now,Close and quit the browser")
        self.driver.quit()