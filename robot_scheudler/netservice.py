#!/usr/bin/python2.6  
# -*- coding: utf-8 -*-  
#encoding=utf-8
'''
Created on 2014年6月15日

@author: kerry
'''

from twisted.internet import reactor, protocol
from base.miglog import miglog
from robot_scheudler.robot_scheduler_center import RobotScheduler


class MIGBaseSchedulerClient(protocol.Protocol):
    def connectionMade(self):
        miglog.log().debug("connection success")
        self.transport.write(self.scheduler.Schduler_Login(self.platform_id, self.machine_id))
    
    def dataReceived(self, data):
        "As soon as any data is received, write it back."
        packet_length,operate_code,data_length = self.chat_logic.UnpackHead(data)
        if(packet_length - 31 <> data_length):
            pass
        if(packet_length<=31):
            pass

            
    
    def connectionLost(self, reason):
        print "connection lost"
    
    def dataWrite(self,data):
        self.transport.write(data)
    
    def __init__(self):
        print "MIGBaseSchedulerClient:init"
        self.scheduler = RobotScheduler()
    
    def set_platform_id(self,platform_id):
        self.platform_id = platform_id
        
    def set_machine_id(self,machine_id):
        self.machine_id = machine_id
        

        
        

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
        