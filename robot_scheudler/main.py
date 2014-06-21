#!/usr/bin/python2.6  
# -*- coding: utf-8 -*-  
#encoding=utf-8

from netservice import MIGInitialScheduler
import base.util

from robot_scheudler.robot_user_mgr import RobotUserMgr

'''
Created on 2014年6月15日

@author: kerry
'''

if __name__ == '__main__':
    initial_scheduler = MIGInitialScheduler()
    initial_scheduler.set_platform_id(10000)
    initial_scheduler.set_machine_id(base.util.GetMac())
    initial_scheduler.Connection("112.124.49.59", 19008)
    initial_scheduler.start_run()