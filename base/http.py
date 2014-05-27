#!/usr/bin/python2.6  
# -*- coding: utf-8 -*-  
#encoding=utf-8

'''
Created on 2014年5月27日

@author: kerry
'''
import httplib
from StringIO import  StringIO
from gzip import GzipFile

class MIGHttpResponse:
    '''
    classdocs
    '''
    __url = ''
    __host =''
    __data = ''

    def __init__(self, url,host):
        '''
        Constructor
        '''
        self.__url = url
        self.__host = host
        
    def HttpMethodGet(self,header={}):
        conn = httplib.HTTPConnection(self.__host)
        headers = {
                   "Host": self.__host,
                   "Connection": "keep-alive",
                   "Cache-Control": "max-age=0",
                   "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                   "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6",
                   "User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36",
                   "ContentType":"application/x-www-form-urlencoded" 
        }
        conn.request(method="GET", url=self.__url,headers = headers)
        response = conn.getresponse()
        if(response.getheader('content-encoding') == 'gzip'):
            data = response.read()
            data2 = GzipFile('','r',0,StringIO(data)).read()
            data = data2
        else:
            data = data = response.read()
        
        self.__data = data
    
    def HttpGetContent(self):
        return self.__data
    
        
        
    
        