#!/usr/bin/python2.6  
# -*- coding: utf-8 -*-  
#encoding=utf-8

'''
Created on 2014年6月21日

@author: kerry
'''
from robot_scheudler import robot_protocol

class RobotConnection(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    def RobotLogin(self,platform_id,uid,robotid):
        self.platform_id = platform_id
        robot_login = robot_protocol.RobotLogin()
        robot_login.make_head(1002,1, 0, 0)
        robot_login.set_platform_id(platform_id)
        robot_login.set_uid(uid)
        robot_login.set_robot_id(robotid)
        return robot_login.packstream()
    
robot_connection = RobotConnection()