#!/usr/bin/python2.6  
# -*- coding: utf-8 -*-  
#encoding=utf-8
'''
Created on 2014年6月21日

@author: kerry
'''
from robot_scheudler import robot_protocol
from robot_connection import robot_connection
from robot_song_mgr import robot_song_mgr
from base.miglog import miglog
class RobotMgr(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    def UnpackHead(self,data):
        packet_head = robot_protocol.PacketHead()
        return  packet_head.unpackhead(data)
        
    def RobotLogin(self,platform_id,uid,robotid):
        return robot_connection.RobotLogin(platform_id, uid, robotid)
    
    def HandselSong(self,data):
        return robot_song_mgr.OnRobotHandselSong(data)
    
robot_mgr = RobotMgr()