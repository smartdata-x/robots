#!/usr/bin/python2.6  
# -*- coding: utf-8 -*-  
#encoding=utf-8

'''
Created on 2014年6月3日

@author: kerry
'''
from twisted.internet import reactor, protocol
from chatlogic import ChatLogic

class MIGBaseSchedulerClient(protocol.Protocol):
    def connectionMade(self):
        print "connection success"
        self.transport.write(self.chat_logic.UserLogin(self.platform_id,self.uid,self.token))
    
    def dataReceived(self, data):
        "As soon as any data is received, write it back."
        packet_length,operate_code,data_length = self.chat_logic.UnpackHead(data)
        if(packet_length - 31 <> data_length):
            pass
        if(packet_length<=31):
            pass
        if(operate_code==1001):
            self.transport.write(self.chat_logic.OnGetUserInfo(data,self.oppotype,self.oppoid))
        if(operate_code==1021):
            self.transport.write(self.chat_logic.OnEnterGroup(data,self.oppoid))
        if(operate_code==1101):
            self.chat_logic.OnTextPrivate(data)
    
    def connectionLost(self, reason):
        print "connection lost"
    
    def dataWrite(self,data):
        self.transport.write(data)
    
    def __init__(self):
        print "MIGBaseSchedulerClient:init"
        self.chat_logic = ChatLogic()
    
    def set_uid(self,uid):
        self.uid = uid
        
    def set_platform_id(self,platform_id):
        self.platform_id = platform_id
        
    def set_token(self,token):
        self.token = token
    
    def set_oppo_id(self,oppoid):
        self.oppoid = oppoid
    
    def set_oppo_type(self,oppotype):
        self.oppotype = oppotype
        
        

class MIGBaseSchedulerFactory(protocol.ClientFactory):
    
    
   
    def __init__(self,platformid,uid,token,oppoid,oppptype):
        print "MIGBaseSchedulerFactory:__init__"
        self.protocol = MIGBaseSchedulerClient
        self.platformid = platformid
        self.uid = uid
        self.token = token
        self.oppoid = oppoid
        self.oppptype = oppptype

        
        

    def clientConnectionFailed(self, connector, reason):
        print "Connection failed - goodbye!"
        reactor.stop()
    
    def clientConnectionLost(self, connector, reason):
        print "Connection lost - goodbye!"
        reactor.stop()
        
    def buildProtocol(self, addr):
        p = protocol.ClientFactory.buildProtocol(self, addr)
        p.set_platform_id(self.platformid)
        p.set_uid(self.uid)
        p.set_token(self.token)
        p.set_oppo_id(self.oppoid)
        p.set_oppo_type(self.oppptype)
        return p
        
class MIGSchedulerClient():
    def Connection(self,host,port):
        f = MIGBaseSchedulerFactory(self.platform_id,self.uid,self.token,self.oppid,self.oppo_type)
        reactor.connectTCP(host, port, f)
        
    def set_uid(self,uid):
        self.uid = uid
    
    def set_platform_id(self,platform_id):
        self.platform_id = platform_id
    
    def set_token(self,token):
        self.token = token
    
    def set_oppid(self,oppid):
        self.oppid = oppid
    
    def set_oppo_type(self,oppo_type):
        self.oppo_type = oppo_type
        
    def start_run(self):
        reactor.run()
        