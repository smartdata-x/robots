#!/usr/bin/python2.6  
# -*- coding: utf-8 -*-  
#encoding=utf-8

import logging
import datetime
'''
Created on 2014年6月6日

@author: Administrator
'''

class MIGLogging(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        filename = 'robots_'+datetime.datetime.now().strftime('%b_%d_%y-%H')+'.log'
        format_str = 'processid :%(process)d  %(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s'
        logging.basicConfig(level=logging.DEBUG,
                format=format_str,
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename= filename,
                filemode='a')
        ##控制台输出
        console = logging.StreamHandler()  
        console.setLevel(logging.INFO)
        console.setLevel(logging.DEBUG) 
        formatter = logging.Formatter(format_str)  
        console.setFormatter(formatter)  
        # 将定义好的console日志handler添加到root logger  
        logging.getLogger('').addHandler(console)  
        
    def DebugLog(self,data):
        logging.debug(data)
    
    def InfoLog(self,data):
        logging.info(data)
    
    def WarningLog(self,data):
        logging.warning(data)
        
    def ErrorLog(self,data):
        logging.error(data)
        
miglogging = MIGLogging()