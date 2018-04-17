# -*- coding: utf-8 -*-

import os
import smtplib
import time
from email.mime.text import MIMEText
pwd = os.getcwd()

#定义发送邮件
def sentmail(file_new):
    #发信邮箱
    mail_from='akrin@mail.com'
    #收信邮箱
    mail_to=['arkin@qq.com']
    #定义正文
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()
    msg=MIMEText(mail_body,_subtype='html',_charset='utf-8')
    #定义标题
    msg['From'] =u"UI-自动化测试"
    msg['Subject']=u"基本功能测试"
    #定义发送时间（不定义的可能有的邮件客户端会不显示发送时间）
    msg['date']=time.strftime('%a, %d %b %Y %H:%M:%S %z')
    smtp=smtplib.SMTP()
    #连接SMTP 服务器
    smtp.connect('smtp.exmail.qq.com')
    #用户名密码
    smtp.login('mail','password')
    smtp.sendmail(mail_from,mail_to,msg.as_string())
    smtp.quit()
    print 'email has send out !'
#查找测试报告，调用发邮件功能
def sendreport():

    result_dir = os.path.abspath(os.path.dirname(pwd) + os.path.sep + "...") + '\\result\\TestRepost\\'
    lists=os.listdir(result_dir)
    lists.sort(key=lambda fn: os.path.getmtime(result_dir+"\\"+fn) if not
    os.path.isdir(result_dir+"\\"+fn) else 0)
    print (u'最新测试生成的报告： '+lists[-2])
    #找到最新生成的文件
    file_new = os.path.join(result_dir,lists[-2])
    print file_new
    #调用发邮件模块
    sentmail(file_new)