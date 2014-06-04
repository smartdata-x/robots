#!/usr/bin/python2.6  
# -*- coding: utf-8 -*-  
#encoding=utf-8

'''
Created on 2014年6月3日

@author: Administrator
'''

from chat import migprotocol
from userconnection import UserConnection
from file_mgr import FileMgr
from userinfo import UserInfo

class ChatLogic(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.user_mgr = UserConnection()
        self.file_mgr = FileMgr()

    def UserLogin(self,platform_id,user_id,token):
        return self.user_mgr.UserLogin(platform_id,user_id,token)
    
    def UnpackHead(self,data):
        packet_head = migprotocol.PacketHead()
        return  packet_head.unpackhead(data)
    
    
########################################################
    def OnGetUserInfo(self,data):
        self.userinfo = self.user_mgr.OnGetUserinfo(data)
        #加入讨论组
        return self.user_mgr.OnAddTypeChat(3,self.userinfo)
    
    def OnEnterGroup(self,data):
        self.user_mgr.OnEnterGroup(data)
        return self.file_mgr.SendSoundFile(self.userinfo)
        
        
        
    