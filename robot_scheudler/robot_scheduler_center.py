#!/usr/bin/python2.6  
# -*- coding: utf-8 -*-  
#encoding=utf-8


from robot_scheudler import robot_protocol
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
    def Schduler_Login(self,platform_id,machine_id):
        login = robot_protocol.LoginPacket()
        login.make_head(2000,1, 0, 0)
        login.set_platform_id(platform_id)
        login.set_machine_id(machine_id)
        return login.packstream()
        
        
        
        