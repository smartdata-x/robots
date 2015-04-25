#!/usr/bin/python2.6  
# -*- coding: utf-8 -*-  
#encoding=utf-8

'''
Created on 2015年4月21日

@author: kerry
'''

#一个请求一个进程
#一个进程中包含多个线程

from base.miglog import miglog
from multiprocessing import Process,Pool,Pipe
from loadrunner.UserModule import UserScheduler

def LoadRunnerUser():
    miglog.log().info("LoadRunnerUser")
    scheduler = UserScheduler()
    scheduler.Start()
def LoadRunnerMusic():
    miglog.log().info("LoadRunnerMusic");
    
class LoaderRunnerScheduler(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    
    def StartUser(self):
        #LoadRunnerUser()
        i = 0
        pool = Pool(processes = 2)
        while(i<2):
            result = pool.apply_async(LoadRunnerUser)
            i = i + 1
        #result = pool.apply_async(LoadRunnerMusic)
        result.get()
        pool.close()


        