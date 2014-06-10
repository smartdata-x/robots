#!/usr/bin/python2.6  
# -*- coding: utf-8 -*-  
#encoding=utf-8

'''
Created on 2014年6月9日

@author: archer
'''

from base.http import MIGHttpMethodPost

class AutoSayHelloBase:
    def __init__(self):
        self.null = 0
        

class AutoSayHello(AutoSayHelloBase):
    def __init__(self):
        AutoSayHelloBase.__init__(self)
        self.url = "http://112.124.49.59/cgi-bin/sayhello.fcgi"
        self.host = "112.124.49.59"
        self.senderId = 10149
        self.msg = ''
        
    def DoSayHello(self, senderId, receiverId, msg):
        http = MIGHttpMethodPost(self.url, self.host)
        data = {'uid':str(senderId),'touid':str(receiverId),'msg':msg}
        http.HttpMethodPost(data=data,urlcode=1)
        print http.HttpGetContent()
        
        #批量发送，设置好发送者账号和消息，每次只需要掉接受者的账号
    def SetSenderId(self, senderId):
        self.senderId = senderId
        
    def SetMessage(self, msg):
        self.msg = msg
        
    def DoSayHelloWithReceiver(self, receiverId):
        self.DoSayHello(self.senderId, receiverId=receiverId, self.msg)
        