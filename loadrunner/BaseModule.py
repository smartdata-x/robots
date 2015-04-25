#!/usr/bin/python 
# -*- coding: utf-8 -*-  
#encoding=utf-8
'''
Created on 2015年4月26日

@author: pro
'''

class BaseModule(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    
    def EventStop(self,request,result):
        pass
    
    def EventException(self,request, exc_info):
        if not isinstance(exc_info, tuple):
            print request
            print exc_info
            raise SystemExit
        print "**** Exception occured in request #%s: %s" % \
          (request.requestID, exc_info)
        