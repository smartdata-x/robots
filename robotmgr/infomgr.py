#!/usr/bin/python2.6  
# -*- coding: utf-8 -*-  
#encoding=utf-8
'''
Created on 2014年6月9日

@author: kerry
'''
from base.http import MIGHttpMethodGet
from xml.etree import ElementTree
import base.util as util
class RobotInfoMgr(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    def GetRobotInfo(self,index,count):
        url = "http://112.124.49.59/cgi-bin/getrobots.fcgi?from="+index+"&count="+count
        host ="112.124.49.59"
        http = MIGHttpMethodGet(url,host)
        http.HttpMethodGet()
        result,content = util.MIGGetResult(http.HttpGetContent())
        if(result==1):
            return content
        else:
            print "GetResult Error"
    
    def GetUserHead(self):
        url = "http://www.5show.com/webservice.asmx/GetVipAlbumList?pageIndex=1&pageSize=10"
        host ="www.5show.com"
        http = MIGHttpMethodGet(url,host)
        http.HttpMethodGet()
        root = ElementTree.fromstring(http.HttpGetContent())
        lst_node = root.getiterator("UserInfo")
        print lst_node
        
        
        