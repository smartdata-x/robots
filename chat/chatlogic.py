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
from im_mgr import ImMgr

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
        self.im_mgr = ImMgr()

    def UserLogin(self,platform_id,user_id,token):
        return self.user_mgr.UserLogin(platform_id,user_id,token)
    
    def UnpackHead(self,data):
        packet_head = migprotocol.PacketHead()
        return  packet_head.unpackhead(data)
    
    
########################################################
    def OnGetUserInfo(self,data,oppotype,oppoid):
        self.userinfo = self.user_mgr.OnGetUserinfo(data)
        #加入讨论组
        return self.user_mgr.OnAddTypeChat(oppotype,self.userinfo,oppoid)
    
    def OnEnterGroup(self,data,oppoid):
        self.user_mgr.OnEnterGroup(data)
        content = "哈哈"
        return self.im_mgr.TextPrivateSend(self.userinfo, oppoid, content)
        #return self.file_mgr.SendSoundFile(self.userinfo)
        
    def OnTextPrivate(self,data):
        self.im_mgr.TextPrivateRecv(data)
        
        
        
    