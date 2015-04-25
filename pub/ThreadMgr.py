#!/usr/bin/python2.6  
# -*- coding: utf-8 -*-  
#encoding=utf-8
'''
Created on 2015年4月26日

@author: pro
'''
from pylib.threadpool import ThreadPool,NoResultsPending,makeRequests
from base.miglog import miglog

class ThreadMgr(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    @classmethod
    def CreateThreadPoolWork(cls,task,num,taskcallback,stopcallback,exceptioncallback):
        main = ThreadPool(num)
        requests = makeRequests(taskcallback,task,stopcallback,exceptioncallback)
        for req in requests:
            main.putRequest(req)
        
        while True:
            try:
                main.poll()
            except KeyboardInterrupt:
                miglog.log().error("**** Interrupted!")
                break
            except NoResultsPending:
                miglog.log().error("**** No pending results.")
                break
            
        if main.dismissedWorkers:
            print "Joining all dismissed worker threads..."
            main.joinAllDismissedWorkers()
        
        