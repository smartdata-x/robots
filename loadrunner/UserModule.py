#!/usr/bin/python 
# -*- coding: utf-8 -*-  
#encoding=utf-8
'''
Created on 2015年4月21日

@author: kerry
'''


from pylib.threadpool import ThreadPool,NoResultsPending,makeRequests
from pub.ThreadMgr import ThreadMgr
from loadrunner.BaseModule import BaseModule
from base.miglog import miglog
from api.Entity import ThirdLoginInfo
from api.UserApi import UserApi
        
        
class UserModule(BaseModule):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    def ThirdLogin(self,data):#第三登陆测试
        #miglog.log().info("ThirdLogin")
        third_info = ThirdLoginInfo()
        third_info.head = "http://tp3.sinaimg.cn/1716373982/180/40041487511/1"
        third_info.imei = "88888"
        third_info.location = "北京 北京"
        third_info.machine = 1
        third_info.nickname = "淘幕天_袁行远"
        third_info.session = "1716373982"
        third_info.sex =  1
        third_info.source  = 1
        print UserApi.ThirdLogin(third_info)
        result = round(4, 5)
        return result
    
        
class UserScheduler(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.user_module = UserModule()
        self.content =  [ 0 for i in range(5000)]
    
       
    def Start(self):
        ThreadMgr.CreateThreadPoolWork(self.content, 100, self.user_module.ThirdLogin,\
                self.user_module.EventStop, self.user_module.EventException)
        #self.user_module.ThirdLogin()
   
        