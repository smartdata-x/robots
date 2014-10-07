#!/usr/bin/python2.6  
# -*- coding: utf-8 -*-  
#encoding=utf-8

'''
Created on 2014年5月27日

@author: kerry
'''
import httplib
import urllib
from StringIO import  StringIO
from gzip import GzipFile

#http base
#若没有自定http头则默认以为chrome浏览器方式
class MIGHttpBase:
    def __init__(self,url,host):
        self.url = url
        self.host = host
        self.data = ''
        self.headers = {
            "Host": self.host,
            "Connection": "keep-alive",
            "Cache-Control": "max-age=0",
            "accept_charset":"utf-8,gbk, *;q=0.7",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6",
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36",
            "ContentType":"application/x-www-form-urlencoded" 
        }
       
    def HttpGetContent(self):
        return self.data


class MIGHttpMethodPost(MIGHttpBase):
    
    def __init__(self,url,host):
        MIGHttpBase.__init__(self, url, host)
        
    def HttpMethodPost(self,data,header={},cookies={},urlcode=0):
        conn = httplib.HTTPConnection(self.host)

        if(urlcode==1):
            data_urlencode = urllib.urlencode(data)
            #print data_urlencode
            post_data = data_urlencode
        else:
            post_data = data
            
            
        conn.request(method="POST", url=self.url, body = str(post_data), headers = self.headers)
        response = conn.getresponse()
        if(response.getheader('content-encoding') == 'gzip'):
            data = response.read()
            data2 = GzipFile('','r',0,StringIO(data)).read()
            data = data2
        else:
            data =  response.read()
        self.data = data
        
        
    
class MIGHttpMethodGet(MIGHttpBase):
    '''
    classdocs
    '''
    def __init__(self,url,host):
        MIGHttpBase.__init__(self, url, host)
        
    def HttpMethodGet(self,header={},cookies={}):
        if(len(header)>0):
            headers = header
        else:
            headers = self.headers
        
        if(len(cookies)>0):
            headers["Cookies"] = cookies
        conn = httplib.HTTPConnection(self.host)
        conn.request(method="GET", url=self.url,headers = headers)
        # 
        response = conn.getresponse()
        print response
        if(response.getheader('content-encoding') == 'gzip'):
            data = response.read()
            data2 = GzipFile('','r',0,StringIO(data)).read()
            data = data2
        else:
            data = data = response.read()
        self.data = data

    
        
        
    
        