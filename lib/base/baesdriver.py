# -*- coding: utf-8 -*-
import time,random,os
from selenium   import  webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select
from lib.base.logger import Logger
pwd =os.getcwd()
logger = Logger(logger='BaseDriver').getlog()
class BaseDriver(object):

    def __init__(self,driver):
        self.driver =driver



    def back(self):
        self.driver.back()
        logger.info("Click back on current page.")

    def forward(self):
        self.driver.forward()
        logger.info("Click forward on current page.")

    def open_url(self,url):
        self.driver.get(url)

    def quit_browser(self):
        self.driver.quit()

    def close(self):
        try:
            self.driver.close()
            logger.info("Close and quit the browser.")
        except NameError as e:
            logger.error("Failed to quit the browser with %s " % e)

    def wait(self,seconds):
        self.driver.implicitly_wait(seconds)
        logger.info("wait for %d seconds." % seconds)

    def get_save_img(self):
        """
            save img
        """
        file_path =os.path.abspath(os.path.dirname(pwd) + os.path.sep + "..") + '\\result\\screenshosts\\'
        rq = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info('Had take screenshot and save to folder ： /screenshots')
        except NameError as e:
            logger.error('Failed to take screenshot! %s'% e)
            self.get_save_img()

    def find_element(self,selector):
        """
        使用 , 切割字符串

        """
        element = ''
        if ',' not in selector:
            return self.driver.find_element_by_id(selector)
        selector_by = selector.split(',')[0]
        selector_value = selector.split(',')[1]

        if selector_by == "i" or selector_by =='id':
            try:
                element = self.driver.find_element_by_id(selector_value)
                logger.info("Had find the element \' %s \' successful " 
                             "by %s via value: %s " % (element.text,selector_by,selector_value))
            except NoSuchElementException as e:
                logger.error("NosuchElementException: %s" % e)
                self.get_save_img()

        elif selector_by == 'n' or selector_by == 'name':
            element = self.driver.find_element_by_name(selector_value)
        elif selector_by =='c' or selector_by =='class_name':
            element = self.driver.find_element_by_class_name(selector_value)
        elif selector_by == 'l' or selector_by == 'link_text':
            element = self.driver.find_element_by_link_text(selector_value)
        elif selector_by == 'p' or selector_by == 'partial_link_text':
            element = self.driver.find_element_by_partial_link_text(selector_value)
        elif selector_by =='t' or selector_by == 'tag_name':
            element = self.driver.find_element_by_tag_name(selector_value)
        elif selector_by == 'x' or selector_by == 'xpath':
            try:
                element = self.driver.find_element_by_xpath(selector_value)
                logger.info("Had find the element \' %s \' successful "
                            "by %s via value: %s " % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s" % e)
                self.get_save_img()
        elif selector_by == "s" or selector_by == 'selector_selector':
            element = self.driver.find_element_by_css_selector(selector_value)
        else:
            raise NameError("Please enter a valid type of targeting elements.")
        return element
    def find_elements(self,selector):
        """
        使用 , 切割字符串

        """
        elements = ''
        if ',' not in selector:
            return self.driver.find_elements_by_id(selector)
        selector_by = selector.split(',')[0]
        selector_value = selector.split(',')[1]

        if selector_by == "i" or selector_by =='id':
            try:
                elements = self.driver.find_elements_by_id(selector_value)
                logger.info("Had find the element \' %s \' successful " 
                             "by %s via value: %s " % selector_by)
            except NoSuchElementException as e:
                logger.error("NosuchElementException: %s" % e)
            self.get_save_img()

        elif selector_by == 'n' or selector_by == 'name':
            elements = self.driver.find_elements_by_name(selector_value)
        elif selector_by =='c' or selector_by =='class_name':
            elements = self.driver.find_elements_by_class_name(selector_value)
        elif selector_by == 'l' or selector_by == 'link_text':
            elements = self.driver.find_elements_by_link_text(selector_value)
        elif selector_by == 'p' or selector_by == 'partial_link_text':
            elements = self.driver.find_elements_by_partial_link_text(selector_value)
        elif selector_by =='t' or selector_by == 'tag_name':
            elements = self.driver.find_elements_by_tag_name(selector_value)
        elif selector_by == 'x' or selector_by == 'xpath':
            try:
                elements = self.driver.find_elements_by_xpath(selector_value)
                logger.info("Had find the element \' %s \' successful "
                            "by %s via value: %s " )
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s" % e)
                self.get_save_img()
        elif selector_by == "s" or selector_by == 'selector_selector':
            elements = self.driver.find_elements_by_css_selector(selector_value)
        else:
            raise NameError("Please enter a valid type of targeting elements.")
        return elements
    def type(self, selector, text):

        el = self.find_element(selector)
        el.clear()
        try:

            el.send_keys(text)
            logger.info("Had type \' %s \' in inputBox" % text)
        except NameError as e:
            logger.error("Failed to type in input box with %s" % e)
            self.get_save_img()

    def attribute_value(self,selector,attribut):

        el = self.find_element(selector)
        try:
            el.get_attribute(attribut)
            logger.info("Get the \' %s \' attribute value" % attribut)

        except NoSuchElementException as e:
            logger.error("NoSuchElementException: %s" % e)
            self.get_save_img()

    def select_index(self,selector,index):
        el = Select(self.find_element(selector))
        try:
            el.select_by_index(index)
            logger.info("Get the \' %s \' " % index)
        except NoSuchElementException as e:
            logger.error("NoSuchElementException: %s" % e)
            self.get_save_img()


    def select_value(self,selector,value):
        el = Select(self.find_element(selector))
        try:
            el.select_by_value(value)

            logger.info("Get the \' %s \' " % value)

        except NoSuchElementException as e:
            logger.error("NoSuchElementException: %s" % e)
            self.get_save_img()

    def select_visible(self,selector,text):
        el = Select(self.find_element(selector))
        try:
            el.select_by_visible_text(text)
            logger.info("Get the \' %s \' " % text)
        except NoSuchElementException as e:
            logger.error("NoSuchElementException: %s" % e)
            self.get_save_img()




    def get_text(self,selector):
        el = self.find_element(selector)
        try:
            text = el.text
            logger.info("Gets the element node value: %s " %text)
            return  text
        except NoSuchElementException as e:
            logger.error("NoSuchElementException: %s" % e)
            self.get_save_img()
    '''
    def clear(self,selector):

        el = self.find_element(selector)
        try:
            el.clear()
            logger.info("Clear text before input box.")
        except NameError as e:
            logger.error("Failed to clear in input box with %s" % e)
            self.get_save_img()
    '''
    def click(self,selector):
        """
            clicks  once button.
        :param selector:
        :return:
        """
        el = self.find_element(selector)
        try:
            time.sleep(2)
            el.click()
            time.sleep(1)
            logger.info("The element \' %s \' was clicked." % el)
        except NameError as e:
            logger.error("Failed to click the element with %s" % e)

    def clicks(self, selector):
        """
            clicks  once button.
        :param selector:
        :return:
        """
        el = self.find_elements(selector)
        try:
            time.sleep(2)
            for i in el:
                el.click()
            time.sleep(1)
            logger.info("The elements \' %s \' was clicked." % el)
        except NameError as e:
            logger.error("Failed to click the element with %s" % e)

    """
        switch to iframe/window
    """

    def switch_frame(self,selector):
        """
          #switch_to_from
        :param selector:

        """
        self.driver.switch_to_frame(selector)


    def switch_default_content(self):
        """
          #switch_to_default_content
        :param selector:
        :return:
        """
        self.driver.switch_to_default_content()

    def smart_wait(self,find):

        for i in range(60):

            if i >=59:
                print "timeout"
                break
            try:
                if find:

                    break
            except:
                print ("wait for find element %s" )
            time.sleep(1)
        return  find

    def click_two(self,selector1,selector2):
        """

        :param selector1:
        :param selector2:
        :return:
        """
        e1 = self.find_element(selector1)
        e2 = self.find_element(selector2)
        try:
            e1.click()
            logger.info("The element \' %s \' was clicked." % e1)
            e2.click()
            logger.info("The element \' %s \' was clicked." % e2)
        except NameError as e:
            logger.error("Failed to click the element with %s" % e)

    def get_title(self):
        """
            Get current page title

        """
        logger.info("Current page title is %s" % self.driver.title)
        return self.driver.title

    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)
        logger.info("Sleep for %d seconds" % seconds)

    def currentime(self):
        time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

    def iselement(self,selector):

        try:
            self.driver.find_element(selector)
            return True
        except:
            return False




