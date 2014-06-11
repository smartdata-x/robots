#!/usr/bin/python2.6  
# -*- coding: utf-8 -*-  
#encoding=utf-8

'''
Created on 2014年6月5日

@author: Administrator
'''


from http import MIGHttpMethodGet
import util
class RobotInfoMgr(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.__GetRobotInfo()
        
    def __GetRobotInfo(self):
        url = "http://112.124.49.59/cgi-bin/getrobots.fcgi?from=0&count=1000"
        host ="112.124.49.59"
        http = MIGHttpMethodGet(url,host)
        http.HttpMethodGet()
        result,content = util.MIGGetResult(http.HttpGetContent())
        if(result==1):
            self.content = content
        else:
            print "GetResult Error"
    
    def GetRobotInfo(self):
        return self.content
        
        
        