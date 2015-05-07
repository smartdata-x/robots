#!/usr/bin/python2.6  
# -*- coding: utf-8 -*-  
#encoding=utf-8

from scheudler.ScheudlerNetSvc import MIGInitialScheduler
import base.util
import os
import sys
import platform
from scheudler.RobotUseMgr import RobotUserMgr
from pub.Config import SingletonConfig

'''0
Created on 2014年6月15日

@author: kerry
'''

if __name__ == '__main__':
    sysstr = platform.system()
    print sysstr
    if(platform.system()=="Darwin" or platform.system()=="Linux"):
        reload(sys)
        sys.setdefaultencoding('utf-8')
    print sys.getdefaultencoding()  
    initial_scheduler = MIGInitialScheduler()
    initial_scheduler.set_platform_id(10000)
    initial_scheduler.set_machine_id(base.util.GetMac())
    initial_scheduler.Connection(SingletonConfig().robothost, SingletonConfig().robotport)
    initial_scheduler.start_run()