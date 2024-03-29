#!/usr/bin/python2.6  
# -*- coding: utf-8 -*-  
#encoding=utf-8

'''
Created on 2014年6月1日

@author: archer
'''
import smtplib
from email.mime.text import MIMEText

class MIGMailBase:
    def __init__(self, host, user, password, mailpostfix):
        self.host = host            #邮箱服务器
        self.sender_name = user
        self.sender_password = password
        self.sender_postfix = mailpostfix

class MIGMailSend(MIGMailBase):
    def __init__(self, host, user, password, mailpostfix):
        MIGMailBase.__init__(self, host, user, password, mailpostfix)
        
    def MailSendBase(self, to_list, subject, content, mailtype):
        #参数检查
        if(type(to_list) != type([1,2]) 
           or type(subject) != type('1')
           or type(content) != type('1')
           or type(mailtype) != type('1')):
            print 'MailSendBase Invalid parameter'
            return False
        
        if((not cmp(mailtype, 'plain'))
           and (not cmp(mailtype, 'html'))):
            print 'MailSendBase Invalid parameter'
            return False
        
        #设置发件人，主题，收件人
        sender = "hello" + "<" + self.sender_name + ">"
        msg = MIMEText(content, _subtype=mailtype)
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = ";".join(to_list)
        
        print msg['To']
        
        try:
            #连接服务器并发送
            #server = smtplib.SMTP()
            server = smtplib.SMTP_SSL()
            server.connect(self.host)
            server.login(self.sender_name, self.sender_password)
            server.sendmail(sender, to_list, msg.as_string())
            server.close()
            return True
        except Exception, e:
            print str(e)
            return False
        
        

    def MailSendText(self, to_list, subject, content):
        self.MailSendBase(to_list, subject, content, 'plain')
    
    
    def MailSendHtml(self, to_list, subject, content):
        self.MailSendBase(to_list, subject, content, 'html')
