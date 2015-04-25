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
from pub.config import SingletonConfig
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
        path = "user/v1/thirdlogin.fcgi"
        url = SingletonConfig().apiurl+path
        dict = info.dict()
        data = urllib.urlencode(dict)
        miglog.log().debug(data)
        #test_url = url+"?"+str(data)
        #return HttpApi.RequestMethodGet(url)
        return HttpApi.RequestMethodPost(url, data)
        
        