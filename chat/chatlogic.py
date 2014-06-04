#!/usr/bin/python2.6  
# -*- coding: utf-8 -*-  
#encoding=utf-8

'''
Created on 2014年6月3日

@author: Administrator
'''

from chat import migprotocol

class ChatLogic(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''

    def UserLogin(self):
        login = migprotocol.LoginPacket()
        login.make_head(1000,2, 0, 0)
        login.set_platform_id(10000)
        login.set_user_id(10149)
        login.set_net_type(0)
        login.set_user_type(1)
        login.set_device(0)
        login.set_token('123213213213123')
        return login.packstream()
    
    def UnpackHead(self,data):
        packet_head = migprotocol.PacketHead()
        return  packet_head.unpackhead(data)
    
    
########################################################
    def OnGetUserInfo(self,data):
        

        
        