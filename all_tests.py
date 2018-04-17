# -*- coding: utf-8 -*-

import os
import time
import unittest
from lib.base import sendreport
from lib.common import HTMLTestRunnerCN
# 读取用例

pwd = os.getcwd()

listcase = pwd+ '\\app\\test_case'


def creatsuite():
    testunit = unittest.TestSuite()
    # discouver方法定义
    discover = unittest.defaultTestLoader.discover(listcase, pattern='test_*.py', top_level_dir=None)
    # discover方法筛选出来的用例，循环添加到测试套件中
    for test_suite in discover:

            testunit.addTests(test_suite)
    return testunit


alltestnames = creatsuite()

# 获取当前时间
now = time.strftime("%Y-%m-%M-%H_%M_%S", time.localtime(time.time()))
# 测试结果报告保存路径

p = pwd +'\\result\\TestReport\\'
filename = p + now + 'Result.html'
fp = file(filename, 'wb')
runner = HTMLTestRunnerCN.HTMLTestRunner(
    stream=fp,
    title=u'UI功能测试',
    description=u'用例执行情况：')

if __name__ == "__main__":
    # 执行测试用例
    runner.run(alltestnames)

    #发送邮件
    #sendreport.sendreport()
