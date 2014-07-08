#!/usr/bin/python2.6  
# -*- coding: utf-8 -*-  
#encoding=utf-8



from base.miglog import miglog
from robot_scheudler import robot_protocol
from robot_scheudler.robot_user_mgr import RobotUserMgr
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
        host = "112.124.49.59"
        port = 19008
        self.robot_user_mgr = RobotUserMgr(host,port)
        
    def UnpackHead(self,data):
        packet_head = robot_protocol.PacketHead()
        return  packet_head.unpackhead(data)
    
    def SchdulerLogin(self,platform_id,machine_id):
        return self.robot_user_mgr.SchdulerLogin(platform_id, machine_id)
    
    def NoticeRobotInfo(self,data):
        robot_login = self.robot_user_mgr.NoticeRobotInfo(data)
    
    def NoticeAssistantInfo(self,data):
        assistant_login = self.robot_user_mgr.NoticeAssistantInfo(data)
    
    def NoticeRobotChatLogin(self,data):
        robot_chat_login = self.robot_user_mgr.NoticeRobotChat(data)
        
        
        
        
        
        