#!/usr/bin/python2.6  
# -*- coding: utf-8 -*-  
#encoding=utf-8


'''
Created on 2015年1月15日

@author: mac
'''
import threading
import ConfigParser
import string
class SingletonConfig(object):
    '''
    classdocs
    '''
    
##单件模式
    objs = {}
    objs_locker =  threading.Lock()
   


    def __new__(cls,*agrs,**kv):
        if cls in cls.objs:
            return cls.objs[cls]['obj']
        cls.objs_locker.acquire()
        try:
            if cls in cls.objs:## double check locking
                return cls.objs[cls]['obj']
            obj = object.__new__(cls)
            #obj.__init__()
            cls.objs[cls] = {'obj':obj,'init':False}
            setattr(cls,'__init__',cls.decorate_init(cls.__init__))
            return cls.objs[cls]['obj']
        finally:
            cls.objs_locker.release()
    
    @classmethod
    def decorate_init(cls,fn):
        def init_wrap(*args):
            if not cls.objs[cls]['init']:
                fn(*args)
                cls.objs[cls]['init'] = True
            return 
        
        return init_wrap


    def __init__(self):
        '''
        Constructor
        '''
        self.chathost = ""
        self.chatport = 0
        
        self.interhost = ""
        
        self.robothost = ""
        self.robotport = 0
        
        self.__read_config__()
        
        
    def __read_config__(self):
        config = ConfigParser.ConfigParser()
        config.read("robot.ini")
        #sections = config.sections()
        
        self.chathost = config.get("chat", "host")
        self.chatport = string.atoi(config.get('chat','port'))
        
        self.interhost = config.get("inter","host")
        
        self.robothost = config.get("robot","host")
        self.robotport =string.atoi(config.get("robot","port"))
    
        
        
        