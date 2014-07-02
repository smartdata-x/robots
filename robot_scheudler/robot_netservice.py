#!/usr/bin/python2.6  
# -*- coding: utf-8 -*-  
#encoding=utf-8
'''
Created on 2014年6月21日

@author: kerry
'''

from twisted.internet import reactor, protocol
from base.miglog import miglog
from robot_mgr import robot_mgr
import sys
import struct


class MIGRobotBaseSchedulerClient(protocol.Protocol):
    def connectionMade(self):
        miglog.log().debug("Robot connection success")
        self.transport.write(robot_mgr.RobotLogin(self.platform_id, self.uid, self.robot_id))
    
    def dataReceived(self, data):
        "As soon as any data is received, write it back."
        pack_stream = self.net_work(data)
        packet_length,operate_code,data_length = robot_mgr.UnpackHead(pack_stream)
        miglog.log().debug("packet_length %d operate_code %d data_length %d",packet_length,operate_code,data_length)
        if(packet_length - 31 <> data_length):
            pass
        if(packet_length<=31):
            pass
        if(operate_code==100):#心跳包回复
            self.transport.write(pack_stream)
        elif (operate_code==1001):
            robot_mgr.HandselSong(pack_stream)
        elif (operate_code==1003):
            robot_mgr.RecordSong(pack_stream)
        
    
    def connectionLost(self, reason):
        print "connection lost"
    
    def dataWrite(self,data):
        self.transport.write(data)
    
    def __init__(self):
        print "MIGBaseSchedulerClient:init"
        self.structFormat = "=i"
        self.prefixLength = struct.calcsize(self.structFormat)
        self._unprocessed = ""
        self.PACKET_MAX_LENGTH = 99999
    
    def set_platform_id(self,platform_id):
        self.platform_id = platform_id
        
    def set_uid(self,uid):
        self.uid = uid
    
    def set_robot_id(self,robot_id):
        self.robot_id = robot_id
        
    def net_work(self,data):
        #取前4个字节
        alldata = self._unprocessed + data
        currentOffset = 0
        fmt = self.structFormat
        self._unprocessed = alldata
        
        while len(alldata) >=(currentOffset + self.prefixLength):
            messageStart = currentOffset + self.prefixLength
            length, = struct.unpack(fmt,alldata[currentOffset:messageStart])
            if length > self.PACKET_MAX_LENGTH:
                self._unprocessed = alldata
                self.lenthLimitExceeded(length)
                return
            messageEnd = currentOffset + length
            if len(alldata) < messageEnd:
                break
            packet = alldata[currentOffset:messageEnd]
            currentOffset = messageEnd
        
        self._unprocessed = alldata[currentOffset:]
        
        return packet
        
        

        
        

class MIGRobotBaseSchedulerFactory(protocol.ClientFactory):
    
    
   
    def __init__(self,platformid,uid,robot_id):
        print "MIGBaseSchedulerFactory:__init__"
        self.protocol = MIGRobotBaseSchedulerClient
        self.platformid = platformid
        self.uid = uid
        self.robot_id = robot_id
        
        

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
        p.set_robot_id(self.robot_id)
        #p.set_machine_id(self.machine_id)
        return p
        
class MIGRobotInitialScheduler():
    def Connection(self,host,port):
        f = MIGRobotBaseSchedulerFactory(self.platform_id,self.uid,self.robot_id)
        reactor.__init__() #因使用进程池，故工作进程会把主进程的reactor拷贝过来，reactor在主进程已经运行，故需要重新初始化
        reactor.connectTCP(host, port, f)
        
    def set_platform_id(self,platform_id):
        self.platform_id = platform_id
    
    def set_uid(self,uid):
        self.uid = uid
    
    def set_robot_id(self,robot_id):
        self.robot_id = robot_id
        
    def start_run(self):
        reactor.run()
        