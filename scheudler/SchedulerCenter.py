#!/usr/bin/python2.6  
# -*- coding: utf-8 -*-  
#encoding=utf-8



from base.miglog import miglog
from scheudler import robot_protocol
from pub.Config import SingletonConfig
from scheudler.RobotUseMgr import RobotUserMgr
'''
Created on 2014年6月15日

@author: kerry
'''



class RobotScheduler(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        #host = "42.121.14.108"
        host = SingletonConfig().robothost
        port = SingletonConfig().robotport
        self.robot_user_mgr = RobotUserMgr(host,port)
        
    def UnpackHead(self,data):
        packet_head = robot_protocol.PacketHead()
        return  packet_head.unpackhead(data)
    
    def SchdulerLogin(self,platform_id,machine_id):
        return self.robot_user_mgr.SchdulerLogin(platform_id, machine_id)
    
    def NoticeRobotInfo(self,data):
        robot_login = self.robot_user_mgr.NoticeRobotInfo(data)
        print robot_login
    
    def NoticeAssistantInfo(self,data):
        assistant_login = self.robot_user_mgr.NoticeAssistantInfo(data)
    
    def NoticeRobotChatLogin(self,data):
        robot_chat_login = self.robot_user_mgr.NoticeRobotChat(data)
        
        
        
        
        
        