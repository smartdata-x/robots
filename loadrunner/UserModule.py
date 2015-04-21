#!/usr/bin/python 
# -*- coding: utf-8 -*-  
#encoding=utf-8
'''
Created on 2015年4月21日

@author: kerry
'''

#from threadpool import ThreadPool,NoResultsPending,NoWorkersAvailable
import loadrunner.threadpool as threadpool
from base.miglog import miglog
        
        
class UserModule(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    def ThirdLogin(self):
        miglog.log().info("ThirdLogin")
    
    def EventStop(self,request,result):
        pass
    
    def EventException(self,request, exc_info):
        pass
        
        
class UserScheduler(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.user_module = UserModule()
        self.content = "123123"
    
    
    def ThreadPool(self,callback):
        requests = threadpool.makeRequests(callback, self.content, self.user_module.EventStop,self.user_module.EventException)
        main = threadpool.ThreadPool(100)
        for req in requests:
            main.putRequest(req)
        
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
       
    def Start(self):
        self.ThreadPool(self.user_module.ThirdLogin)
   
        