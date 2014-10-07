#!/usr/bin/python2.6  
# -*- coding: utf-8 -*-  
#encoding=utf-8

'''
Created on 2014年6月5日

@author: Administrator
'''

#import threadpool
#from threadpool import ThreadPool,NoResultsPending,NoWorkersAvailable
import json
import time
from base.httpinterface import MigHttpInterFace
from chat.netservice import MIGSchedulerClient
from multiprocessing import Process,Pool,Pipe
from base.miglog import  miglog
import  os


    
def ChatRobotSatrt(data):
    uid = int(data["id"])
    client = MIGSchedulerClient()
    token ='414c1edda11bfec34d63b99deada4235'
    client.set_platform_id(data["platform"])
    client.set_token(token)
    client.set_uid(uid)
    client.set_oppid(10108)
    client.set_oppo_type(1)
    client.Connection(data["host"],data["port"])
    client.start_run()
    
    

    
class ChatMgr(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.platform = 10000
        self.chathost = "112.124.49.59"
        #self.chathost = "42.121.14.108"
        self.port = 17000
        self.__GetRobotInfo()
        
    def __GetRobotInfo(self):
        self.content = MigHttpInterFace.GetRobotInfo(3, 3)
        
    
    def ChatRobotSatrt(self):
        i = 0
        for element in self.content:
            i = i +1
        #print i
        pool = Pool(processes=i)
        for element in self.content:
            element["platform"] = self.platform
            element["host"] = self.chathost
            element["port"] = self.port
            element["process_file"] = i 
            result = pool.apply_async(ChatRobotSatrt, [element])
        pool.close()
        pool.join()
        
#reactor不能在线程池中使用 故换成进程池
'''        
    def ChatRobotRun(self,data):
        uid = int(data["id"])
        client = MIGSchedulerClient()
        token ='414c1edda11bfec34d63b99deada4235'
        client.set_platform_id(self.platform)
        client.set_token(token)
        client.set_uid(uid)
        client.set_oppid(10148)
        client.set_oppo_type(1)
        client.Connection(self.chathost,self.port)
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
'''
    
        
    
    
        
        