#!/usr/bin/python2.6  
# -*- coding: utf-8 -*-  
#encoding=utf-8

'''
Created on 2014年6月5日

@author: Administrator
'''

import threadpool
from threadpool import ThreadPool,NoResultsPending,NoWorkersAvailable
import json
from base.robotinfos import RobotInfoMgr
import time
from chat.netservice import MIGSchedulerClient

class ChatMgr(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.__GetRobotInfo()
        
    def __GetRobotInfo(self):
        robot_mgr = RobotInfoMgr()
        self.content = robot_mgr.GetRobotInfo()
        
    def ChatRobotRun(self,data):
           client = MIGSchedulerClient()
           uid = 10149
           platform = 10000
           token ='414c1edda11bfec34d63b99deada4235'
           client.set_platform_id(platform)
           client.set_token(token)
           client.set_uid(uid)
           client.set_oppid(10148)
           client.set_oppo_type(1)
           client.Connection("112.124.49.59",17000)
           client.start_run()
    
    def ChatRobotSatrt(self):
        #data = ""
        i = 0
        for element in self.content:
            i = i +1
            
        requests = threadpool.makeRequests(self.ChatRobotRun, self.content, self.ChatRobotStop, self.ChatRobotException)
        main = threadpool.ThreadPool(i)
        for req in requests:
            main.putRequest(req)
            #print "Work request #%s added." % req.requestID
        
        while True:
            try:
                main.poll()
            except KeyboardInterrupt:
                print "**** Interrupted!"
                break
            except NoResultsPending:
                print "**** No pending results."
                break
            
        if main.dismissedWorkers:
            print "Joining all dismissed worker threads..."
            main.joinAllDismissedWorkers()
        
    def ChatRobotException(self,request, exc_info):
        if not isinstance(exc_info, tuple):
            print request
            print exc_info
            raise SystemExit
        print "**** Exception occured in request #%s: %s" % \
          (request.requestID, exc_info)
    
    def ChatRobotStop(self,request,result):
        pass
    
    
        
    
    
        
        