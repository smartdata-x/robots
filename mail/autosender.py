#!/usr/bin/python2.6  
# -*- coding: utf-8 -*-  
#encoding=utf-8

'''
Created on 2014年6月1日

@author: archer
'''
from base.mail import MIGMailSend

class AutoSendBase:
    def __init__(self):
        #do nothing
        print 'init'

class AutoSendMail(AutoSendBase):
    def __init__(self):
        AutoSendBase.__init__(self)
        
    def ASMParserUserInfo(self):
        return 'user' 'password'
    
    def ASMParserMailPostfix(self):
        return 'miglab.com'
    
    def ASMParserMailContent(self):
        return 'hello world'
    
    def ASMParserToList(self):
        return 'archer@miglab.com'
    
    def ASMParserSubject(self):
        return 'Hello'
    
    def ASMDoStep(self):
        userinfo = self.ASMParserUserInfo();
        sender = MIGMailSend('host', 
                             userinfo[0],
                             userinfo[1], 
                             self.ASMParserMailPostfix(),
                             );
        sender.MailSendText(self.ASMParserToList(),
                             self.ASMParserSubject(), 
                             self.ASMParserMailContent())

