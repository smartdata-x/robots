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
        #参数检查
        if(type(senderId) != type(1) 
           or type(receiverId) != type(1) 
           or type(msg) != type('1')):
            print 'DoSayHello Invalid Parameter'
            return False
        
        http = MIGHttpMethodPost(self.url, self.host)
        data = {'uid':str(senderId),'touid':str(receiverId),'msg':msg}
        print data
        http.HttpMethodPost(data=data,urlcode=1)
        print http.HttpGetContent()
        
        
        
    #批量发送，设置好发送者账号和消息，每次只需要掉接受者的账号
    def SetSenderId(self, senderId):
        #参数检查
        if type(senderId) != type(1):
            print 'SetSenderId Invalid Parameter'
            return False
            
        self.senderId = senderId
        
        
        
    def SetMessage(self, msg):
        #参数检查
        if type(msg) != type('1'):
            print 'SetMessage Invalid Parameter'
            return False
            
        self.msg = msg
        
        
        
    def DoSayHelloAll(self, receiverId):
        #参数检查
        if type(receiverId) != type(1):
            print 'DoSayHelloAll Invalid Parameter'
            return False
            
        self.DoSayHello(self.senderId, receiverId, self.msg)
        