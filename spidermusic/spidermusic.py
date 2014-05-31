#!/usr/bin/python2.6  
# -*- coding: utf-8 -*-  
#encoding=utf-8


'''
Created on 2014年5月31日

@author: kerry
'''
from kowuspider import SpiderKuWo
from base.http import MIGHttpMethodGet
import base.util as util


class SpiderMusic():
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.spider = SpiderKuWo()
    
        
    def GetNewMuisc(self,url,host):
        http = MIGHttpMethodGet(url,host)
        http.HttpMethodGet()
        print http.HttpGetContent()
        result,self.content = util.MIGGetResult(http.HttpGetContent())
        return result
    
    def GetMuiscInfos(self):
        for element in self.content:
            self.spider.SpidertKuWoMusicInfo(element["name"],element["singer"])
            
        
        