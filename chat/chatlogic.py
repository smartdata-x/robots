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
from error_mgr import ErrorMgr

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
        self.error = ErrorMgr()
        #self.callback = callback

    def UserLogin(self,platform_id,user_id,token):
        return self.user_mgr.UserLogin(platform_id,user_id,token)
    
    def UnpackHead(self,data):
        packet_head = migprotocol.PacketHead()
        return  packet_head.unpackhead(data)
    
    
########################################################
    def OnGetUserInfo(self,data,oppotype,oppoid):
        self.userinfo = self.user_mgr.OnGetUserinfo(data)
        return self.user_mgr.OnAddTypeChat(oppotype,self.userinfo,oppoid)
    
    def OnEnterGroup(self,data,oppoid,oppotype):
        self.userinfo.set_session(self.user_mgr.OnEnterGroup(data))
        print self.userinfo.get_session()
        
    def OnTextPrivate(self,callback,data):
        return self.im_mgr.TextPrivateRecv(data,callback,self.userinfo)
    
    def OnErrorInfo(self,data):
        return self.error.ErrorMsg(data)
        
        
        
        
        
    