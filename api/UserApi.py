#!/usr/bin/python 
# -*- coding: utf-8 -*-  
#encoding=utf-8
'''
Created on 2015年4月21日

@author: kerry
'''

from api.Entity import ThirdLoginInfo
from api.HttpApi import HttpApi
from base.miglog import miglog
import urllib
class UserApi(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    @classmethod
    def ThirdLogin(cls,info):
        path = "abheg/user/1/thirdlogin.fcgi"
        dict = info.dict()
        data = urllib.urlencode(dict)
        miglog.log().debug(data)
        return HttpApi.RequestMethodPost(path, data)
        
        