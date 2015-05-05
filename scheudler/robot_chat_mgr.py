#!/usr/bin/python2.6  
# -*- coding: utf-8 -*-  
#encoding=utf-8
'''
Created on 2014年7月7日

@author: kerry
'''
from scheudler import robot_protocol
from base.miglog import miglog

class RobotChatMgr(object):
    '''
    classdocs
    '''


    def __init__(self,):
        '''
        Constructor
        '''
        self.platformid = 0
        self.uid = 0
        self.oppid = 0
        
    def UnpackHead(self,data):
        packet_head = robot_protocol.PacketHead()
        return  packet_head.unpackhead(data)
    
    def RobotChatLogin(self,platform_id,uid,oppid):
        self.platformid = platform_id
        self.uid = uid
        self.oppid = oppid
        robot_chat_login =  robot_protocol.RobotChatLogin()
        robot_chat_login.make_head(1000, 1, 0, 0)
        robot_chat_login.set_platform_id(platform_id)
        robot_chat_login.set_uid(uid)
        return robot_chat_login.packstream()
    
    def RobotJoinChat(self):
        robot_req_info = robot_protocol.ReqOppstionInfo()
        robot_req_info.make_head(1020, 1, 0, 0)
        robot_req_info.set_platform_id(self.platformid)
        robot_req_info.set_uid(self.uid)
        robot_req_info.set_oppstion_id(self.oppid)
        robot_req_info.set_type(1);
        return robot_req_info.packstream()

robot_chat_mgr = RobotChatMgr()
        