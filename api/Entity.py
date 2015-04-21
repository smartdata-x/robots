#!/usr/bin/python 
# -*- coding: utf-8 -*-  
#encoding=utf-8
'''
Created on 2015年4月21日

@author: kerry
'''

class ThirdLoginInfo(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.source = 0 #来源
        self.machine = 0 #机型
        self.nickname = ""
        self.sex = 0
        self.session = ""
        self.bithiday = ""
        self.location = ""
        self.head = ""
        self.imei =""
        
    def dict(self):
        dict = {}
        dict["source"] = self.source
        dict["machine"] = self.machine
        dict["nickname"] = self.nickname
        dict["sex"] = self.sex
        dict["session"] =self.session
        dict["birthday"] = self.bithiday
        dict["location"] = self.location
        dict["head"] = self.head
        dict["imei"] = self.imei
        return dict