#!/usr/bin/python2.6  
# -*- coding: utf-8 -*-  
#encoding=utf-8
'''
Created on 2014年7月1日

@author: kerry
'''
from robot_scheudler import robot_protocol
from base.miglog import miglog
from musicmgr.sendmusic import AutoSendMusic

class AssistantMgr(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.uid = 0
        
    def UnpackHead(self,data):
        packet_head = robot_protocol.PacketHead()
        return  packet_head.unpackhead(data)
        
    def AssistantLogin(self,platform_id,uid,nickname):
        self.platformid = platform_id
        self.uid = uid
        self.nickname = nickname
        assistant_login =  robot_protocol.AssistantLogin()
        assistant_login.make_head(2101, 1, 0, 0)
        assistant_login.set_platform_id(platform_id)
        assistant_login.set_uid(uid)
        return assistant_login.packstream()
    
    def NoticeAssistantHandlse(self,data):
        handlse_song = robot_protocol.NoticeAssistantHandlseSong()
        handlse_song.unpackstream(data)
        #赠送给用户
        handlselist =[ 0 for i in range(0)]
        handlselist = handlse_song.gethandlselist()
        if(len(handlselist)>0):
            for robot in handlselist:
                send_music = AutoSendMusic();
                send_music.DoSendMusic(self.uid,robot.get_uid(),robot.get_songid(), robot.get_message())
                
                
        
assistant_mgr = AssistantMgr()