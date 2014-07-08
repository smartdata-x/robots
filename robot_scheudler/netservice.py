#!/usr/bin/python2.6  
# -*- coding: utf-8 -*-  
#encoding=utf-8
'''
Created on 2014年6月15日

@author: kerry
'''

from twisted.internet import reactor, protocol
from base.miglog import miglog
from base.net_work import NetData
from robot_scheudler.robot_scheduler_center import RobotScheduler
import struct



class MIGBaseSchedulerClient(protocol.Protocol):

    def connectionMade(self):
        miglog.log().debug("connection success")
        self.transport.write(self.scheduler.SchdulerLogin(self.platform_id, self.machine_id))
    
    def dataReceived(self, data):
        "As soon as any data is received, write it back."
        pack_stream,result = self.netdata.net_wok(data)
        miglog.log().debug("result %d",result)
        if(result==0):
            return
        packet_length,operate_code,data_length = self.scheduler.UnpackHead(pack_stream)
        miglog.log().debug("packet_length %d operate_code %d data_length %d",packet_length,operate_code,data_length)
        if(packet_length - 31 <> data_length):
            return
        if(packet_length<=31):
            return
        if (operate_code==1000):
            self.scheduler.NoticeRobotInfo(pack_stream)
        elif(operate_code==2100):
            self.scheduler.NoticeAssistantInfo(pack_stream)
        elif(operate_code==1004):
            self.scheduler.NoticeRobotChatLogin(pack_stream)
    
    def connectionLost(self, reason):
        print "connection lost"
    
    def dataWrite(self,data):
        self.transport.write(data)
    
    def __init__(self):
        print "MIGBaseSchedulerClient:init"
        self.netdata = NetData()
        self.scheduler = RobotScheduler()
    
    def set_platform_id(self,platform_id):
        self.platform_id = platform_id
        
    def set_machine_id(self,machine_id):
        self.machine_id = machine_id
        
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
        


class MIGBaseSchedulerFactory(protocol.ClientFactory):
    
    
   
    def __init__(self,platformid,machine_id):
        print "MIGBaseSchedulerFactory:__init__"
        self.protocol = MIGBaseSchedulerClient
        self.platformid = platformid
        self.machine_id = machine_id
        
        

    def clientConnectionFailed(self, connector, reason):
        print "Connection failed - goodbye!"
        reactor.stop()
    
    def clientConnectionLost(self, connector, reason):
        print "Connection lost - goodbye!"
        reactor.stop()
        
    def buildProtocol(self, addr):
        p = protocol.ClientFactory.buildProtocol(self, addr)
        p.set_platform_id(self.platformid)
        p.set_machine_id(self.machine_id)
        return p
        
class MIGInitialScheduler():
    def Connection(self,host,port):
        f = MIGBaseSchedulerFactory(self.platform_id,self.machine_id)
        reactor.connectTCP(host, port, f)
        
    def set_platform_id(self,platform_id):
        self.platform_id = platform_id
    
    def set_machine_id(self,machine_id):
        self.machine_id = machine_id
        
    def start_run(self):
        reactor.run()
        