#!/usr/bin/python 
# -*- coding: utf-8 -*-  
#encoding=utf-8
'''
Created on 2015年4月26日

@author: pro
'''
from api.Entity import ThirdLoginInfo
from api.HttpApi import HttpApi
from base.miglog import miglog
from pub.config import SingletonConfig
import urllib

class MusicApi(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        
    @classmethod
    def GetDimensions(cls,info):
        path = "music/v1/getdimensions.fcgi"
        url = SingletonConfig().apiurl+path
        dict = info.dict()
        data = urllib.urlencode(dict)
        miglog.log().debug(data)
        neturl = url+"?"+str(data)
        return HttpApi.RequestMethodGet(neturl)
    
    @classmethod
    def GetCltSongs(cls,info):
        path = "music/v1/getcltsongs.fcgi"
        url = SingletonConfig().apiurl+path
        dict = info.dict()
        data = urllib.urlencode(dict)
        miglog.log().debug(data)
        neturl = url+"?"+str(data)
        return HttpApi.RequestMethodGet(neturl)

    @classmethod
    def GetNearMusic(cls,info):
        path = "music/v1/nearmusic.fcgi"
        url = SingletonConfig().apiurl+path
        dict = info.dict()
        data = urllib.urlencode(dict)
        miglog.log().debug(data)
        neturl = url+"?"+str(data)
        return HttpApi.RequestMethodGet(neturl)

    @classmethod
    def GetNearUser(cls,info):
        path = "soc/v1/nearuser.fcgi"
        url = SingletonConfig().apiurl+path
        dict = info.dict()
        data = urllib.urlencode(dict)
        miglog.log().debug(data)
        neturl = url+"?"+str(data)
        return HttpApi.RequestMethodGet(neturl)
    
    @classmethod
    def SetCurrentSong(cls,info):
        path = "music/v1/recordcursong.fcgi"
        url = SingletonConfig().apiurl+path
        dict = info.dict()
        data = urllib.urlencode(dict)
        miglog.log().debug(data)
        return HttpApi.RequestMethodPost(url, data)
        