#!/usr/bin/python2.6  
# -*- coding: utf-8 -*-  
#encoding=utf-8
'''
Created on 2014年7月7日

@author: kerry
'''

from twisted.internet import reactor, protocol
from base.miglog import miglog
#from robot_chat_mgr import robot_chat_mgr
from base.net_work import NetData
import sys
import struct


class MIGChatBaseSchedulerClient(protocol.Protocol):
    def connectionMade(self):
        miglog.log().debug("Chat connection success")
        self.transport.write(robot_chat_mgr.RobotChatLogin(self.platform_id, self.robotid,self.uid))
    
    def dataReceived(self, data):
        "As soon as any data is received, write it back."
        
        #处理粘包问题
        #pack_stream,result = self.net_work(data)
        pack_stream,result = self.netdata.net_wok(data)
        miglog.log().debug("result %d",result)
        if(result==0):
            return
        packet_length,operate_code,data_length = robot_chat_mgr.UnpackHead(pack_stream)
        miglog.log().debug("packet_length %d operate_code %d data_length %d data %d",packet_length,operate_code,data_length,len(pack_stream))
        if(packet_length - 31 <> data_length):
            return
        if(packet_length<=31):
            return
        if(packet_length<>len(pack_stream)):
            miglog.log().debug("===========")
            return 
        if(operate_code==100):#心跳包回复
            self.transport.write(pack_stream)
        if(operate_code==1001):#登陆成功
            self.transport.write(robot_chat_mgr.RobotJoinChat())
            
        
    
    def connectionLost(self, reason):
        print "connection lost"
    
    def dataWrite(self,data):
        self.transport.write(data)
    
    def __init__(self):
        print "MIGChatBaseSchedulerClient:init"
        self.netdata = NetData()

    
    def set_platform_id(self,platform_id):
        self.platform_id = platform_id
        
    def set_uid(self,uid):
        self.uid = uid
    
    def set_robotid(self,robotid):
        self.robotid = robotid
        
        
        

class MIGChatBaseSchedulerFactory(protocol.ClientFactory):
    
    
   
    def __init__(self,platformid,uid,robotid):
        print "MIGChatBaseSchedulerFactory:__init__"
        self.protocol = MIGChatBaseSchedulerClient
        self.platformid = platformid
        self.uid = uid
        self.robotid = robotid
        
        

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
        p.set_robotid(self.robotid)
        return p
        
class MIGChatInitialScheduler():
    def Connection(self,host,port):
        f = MIGChatBaseSchedulerFactory(self.platform_id,self.uid,self.robotid)
        reactor.__init__() #因使用进程池，故工作进程会把主进程的reactor拷贝过来，reactor在主进程已经运行，故需要重新初始化
        reactor.connectTCP(host, port, f)
        
    def set_platform_id(self,platform_id):
        self.platform_id = platform_id
    
    def set_uid(self,uid):
        self.uid = uid
    
    def set_robotid(self,robotid):
        self.robotid = robotid
        
    def start_run(self):
        reactor.run()
        