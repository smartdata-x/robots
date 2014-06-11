#!/usr/bin/python2.6  
# -*- coding: utf-8 -*-  
#encoding=utf-8

'''
Created on 2014年6月1日

@author: archer
'''
from base.mail import MIGMailSend
from base.http import MIGHttpMethodGet
import base.util as gUtil
import base64

class AutoSendBase:
    def __init__(self):
        self.contentUrl = "http://112.124.49.59/cgi-bin/getspreadmail.fcgi"
        self.contentHost = "112.124.49.59"
        self.toListUrl = 'http://112.124.49.59/cgi-bin/getmailinfo.fcgi?from=%d&count=%d'
        self.toListHost = '112.124.49.59'

class AutoSendMail(AutoSendBase):
    def __init__(self):
        AutoSendBase.__init__(self)
        
    def ASMParserSenderInfo(self):
        return 'archer@miglab.com', ''
    
    def ASMParserMailPostfix(self):
        return 'miglab.com'
    
    def ASMParserMailSubjectAndContent(self):
        http = MIGHttpMethodGet(self.contentUrl, self.contentHost)
        http.HttpMethodGet()
        
        result, contentText = gUtil.MIGGetResult(http.HttpGetContent())
        
        mailContent = contentText['content']
        mailSubject = contentText['title']
        
        mailSubject = base64.b64decode(mailSubject)
        mailContent = base64.b64decode(mailContent)
        
        return mailSubject, mailContent
    
    def ASMParserToList(self, fromto=0, count=100):
        
        toListUrl = self.toListUrl % (fromto, count)
        
        print toListUrl
        
        http = MIGHttpMethodGet(toListUrl, self.toListHost)
        http.HttpMethodGet()
        
        result, toListText = gUtil.MIGGetResult(http.HttpGetContent())
        
        toList = []
        for i in toListText:
            toList.append(i['name'])
        
        return toList
    
    def ASMParserHost(self):
        return 'smtp.qq.com'
    
    def ASMDoSend(self):
        senderinfo = self.ASMParserSenderInfo()
        
        mailInfo = self.ASMParserMailSubjectAndContent()
        
        sender = MIGMailSend(self.ASMParserHost(), 
                             senderinfo[0],
                             senderinfo[1], 
                             self.ASMParserMailPostfix(),
                             )
                             
        sender.MailSendText(self.ASMParserToList(1, 4),
                             mailInfo[0], 
                             mailInfo[1]
                             )
        
        print 'The mail sending is finished'

