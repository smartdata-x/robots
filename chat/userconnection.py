#!/usr/bin/python2.6  
# -*- coding: utf-8 -*-  
#encoding=utf-8

'''
Created on 2014年6月4日

@author: kerry
'''
from chat import migprotocol
from userinfo import UserInfo
class UserConnection(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    def UserLogin(self,platform_id,user_id,token):
        login = migprotocol.LoginPacket()
        login.make_head(1000,2, 0, 0)
        login.set_platform_id(platform_id)
        login.set_user_id(user_id)
        login.set_net_type(0)
        login.set_user_type(1)
        login.set_device(0)
        login.set_token(token)
        return login.packstream()
    
    def OnAddTypeChat(self,group_type,userinfo):
        opptioninfo  = migprotocol.ReqOpptionInfo()
        opptioninfo.make_head(1020,2, 0, 0)
        opptioninfo.set_platform_id(userinfo.get_platform_id())
        opptioninfo.set_user_id(userinfo.get_uid())
        opptioninfo.set_oppostion_id(10150)
        opptioninfo.set_type(group_type)
        opptioninfo.set_token(userinfo.get_token())
        return opptioninfo.packstream()
        
    def OnGetUserinfo(self,data):
        loginsucess = migprotocol.LoginSucess()
        loginsucess.unpackstream(data)
        userinfo = UserInfo()
        userinfo.set_platform_id(loginsucess.get_platform_id())
        userinfo.set_uid(loginsucess.get_user_id())
        userinfo.set_nicknumber(loginsucess.get_nicknumber())
        userinfo.set_nickname(loginsucess.get_nickname())
        userinfo.set_head_url(loginsucess.get_head_url())
        userinfo.set_token(loginsucess.get_token())
        return userinfo
    

    def OnEnterGroup(self,data):
        oppoinfo = migprotocol.OppositionInfo()
        oppoinfo.unpackstream(data)
        print "platform_id:",oppoinfo.get_platform_id()
        print "oppoid:", oppoinfo.get_oppo_id()
        print "nickname",oppoinfo.get_oppo_nickname()
        
        
        
        
        