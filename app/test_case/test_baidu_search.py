# -*- coding: utf-8 -*-
import unittest
from app.module.homepage import search_baidu
from lib.base import itembase
from lib.base.logger import Logger

logger = Logger(logger="BaiDuSearch").getlog()
class BaiDuSearch(itembase.Base):
    u"""百度搜索"""

    def test_search(self):
        """搜索"""
        self.login()
        driver = self.driver
        bd = search_baidu.Search(self.driver)
        bd.search_input(u"selenium")
        bd.click_query()
        logger.info(u"百度搜索：selenium  测试通过")

        driver.quit()

if __name__ == '__main__':
    unittest.main()
