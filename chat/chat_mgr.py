#!/usr/bin/python2.6  
# -*- coding: utf-8 -*-  
#encoding=utf-8

'''
Created on 2014年6月5日

@author: Administrator
'''

import threadpool
from base.robotinfos import RobotInfoMgr

class ChatMgr(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
    def __GetRobotInfo(self):
        robot_mgr = RobotInfoMgr()
        self.content = robot_mgr.GetRobotInfo()
        
        