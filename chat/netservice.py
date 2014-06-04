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
        self.transport.write(self.chat_logic.UserLogin())
    
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
        print "init"
        self.chat_logic = ChatLogic()
        

class MIGBaseSchedulerFactory(protocol.ClientFactory):
    protocol = MIGBaseSchedulerClient

    def clientConnectionFailed(self, connector, reason):
        print "Connection failed - goodbye!"
        reactor.stop()
    
    def clientConnectionLost(self, connector, reason):
        print "Connection lost - goodbye!"
        reactor.stop()
        
class MIGSchedulerClient():
    def Connection(self,host,port):
        f = MIGBaseSchedulerFactory()
        reactor.connectTCP(host, port, f)
        reactor.run()