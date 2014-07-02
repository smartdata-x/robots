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
from base.net_work import NetData
import sys
import struct


class MIGAssistantBaseSchedulerClient(protocol.Protocol):
    def connectionMade(self):
        miglog.log().debug("Assistant connection success")
        self.transport.write(assistant_mgr.AssistantLogin(self.platform_id, self.uid, self.nickname))
    
    def dataReceived(self, data):
        "As soon as any data is received, write it back."
        
        #处理粘包问题
        #pack_stream,result = self.net_work(data)
        pack_stream,result = self.netdata.net_wok(data)
        miglog.log().debug("result %d",result)
        if(result==0):
            return
        packet_length,operate_code,data_length = assistant_mgr.UnpackHead(pack_stream)
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
        elif(operate_code==2110):
            assistant_mgr.NoticeAssistantHandlse(pack_stream)
        
    
    def connectionLost(self, reason):
        print "connection lost"
    
    def dataWrite(self,data):
        self.transport.write(data)
    
    def __init__(self):
        print "MIGBaseSchedulerClient:init"
        self.netdata = NetData()
        '''
        self.structFormat = "=i"
        self.prefixLength = struct.calcsize(self.structFormat)
        self._unprocessed = ""
        self.PACKET_MAX_LENGTH = 99999
        '''
    
    def set_platform_id(self,platform_id):
        self.platform_id = platform_id
        
    def set_uid(self,uid):
        self.uid = uid
    
    def set_nickname(self,nickname):
        self.nickname = nickname
        
    '''
    def net_work(self,data):
        #取前4个字节
        alldata = self._unprocessed + data
        currentOffset = 0
        fmt = self.structFormat
        self._unprocessed = alldata
        miglog.log().debug("alldata %d unprocessed %d data %d",len(alldata),len(self._unprocessed),len(data))
        while len(alldata) >=(currentOffset + self.prefixLength):
            messageStart = currentOffset + self.prefixLength
            length, = struct.unpack(fmt,alldata[currentOffset:messageStart])
            if length > self.PACKET_MAX_LENGTH:
                self._unprocessed = alldata
                self.lenthLimitExceeded(length)
                return
            messageEnd = currentOffset + length
            miglog.log().debug("length %d len(dlldata) %d messageEnd(%d)",length,len(alldata),messageEnd)
            if len(alldata) < messageEnd:
                packet = ""
                result = 0
                miglog.log().debug("=====================")
                break
            packet = alldata[currentOffset:messageEnd]
            currentOffset = messageEnd
            result = 1
        
        self._unprocessed = alldata[currentOffset:]
        return packet,result
        '''

        
        

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
        