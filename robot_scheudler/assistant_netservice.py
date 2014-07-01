#!/usr/bin/python2.6  
# -*- coding: utf-8 -*-  
#encoding=utf-8
'''
Created on 2014年7月1日

@author: kerry
'''

from twisted.internet import reactor, protocol
from base.miglog import miglog
from assistant_mgr import assistant_mgr
import sys


class MIGAssistantBaseSchedulerClient(protocol.Protocol):
    def connectionMade(self):
        miglog.log().debug("Assistant connection success")
        self.transport.write(assistant_mgr.AssistantLogin(self.platform_id, self.uid, self.nickname))
    
    def dataReceived(self, data):
        "As soon as any data is received, write it back."
        packet_length,operate_code,data_length = assistant_mgr.UnpackHead(data)
        miglog.log().debug("packet_length %d operate_code %d data_length %d",packet_length,operate_code,data_length)
        if(packet_length - 31 <> data_length):
            pass
        if(packet_length<=31):
            pass
        if(operate_code==100):#心跳包回复
            self.transport.write(data)
        elif(operate_code==2110):
            assistant_mgr.NoticeAssistantHandlse(data)
        
    
    def connectionLost(self, reason):
        print "connection lost"
    
    def dataWrite(self,data):
        self.transport.write(data)
    
    def __init__(self):
        print "MIGBaseSchedulerClient:init"
    
    def set_platform_id(self,platform_id):
        self.platform_id = platform_id
        
    def set_uid(self,uid):
        self.uid = uid
    
    def set_nickname(self,nickname):
        self.nickname = nickname
        

        
        

class MIGAssistantBaseSchedulerFactory(protocol.ClientFactory):
    
    
   
    def __init__(self,platformid,uid,nickname):
        print "MIGBaseSchedulerFactory:__init__"
        self.protocol = MIGAssistantBaseSchedulerClient
        self.platformid = platformid
        self.uid = uid
        self.nickname = nickname
        
        

    def clientConnectionFailed(self, connector, reason):
        print "Connection failed - goodbye!"
        reactor.stop()
    
    def clientConnectionLost(self, connector, reason):
        print "Connection lost - goodbye!"
        #自行退出进程
        reactor.stop()
        sys.exit(0)
        
    def buildProtocol(self, addr):
        p = protocol.ClientFactory.buildProtocol(self, addr)
        p.set_platform_id(self.platformid)
        p.set_uid(self.uid)
        p.set_nickname(self.nickname)
        return p
        
class MIGAssistantInitialScheduler():
    def Connection(self,host,port):
        f = MIGAssistantBaseSchedulerFactory(self.platform_id,self.uid,self.nickname)
        reactor.__init__() #因使用进程池，故工作进程会把主进程的reactor拷贝过来，reactor在主进程已经运行，故需要重新初始化
        reactor.connectTCP(host, port, f)
        
    def set_platform_id(self,platform_id):
        self.platform_id = platform_id
    
    def set_uid(self,uid):
        self.uid = uid
    
    def set_nickname(self,nickname):
        self.nickname = nickname
        
    def start_run(self):
        reactor.run()
        