#!/usr/bin/python 
# -*- coding: utf-8 -*-  
#encoding=utf-8
'''
Created on 2015年4月21日

@author: kerry
'''

from base.http import MIGHttpMethodGet,MIGHttpMethodPost
from base.miglog import miglog
import urlparse
import json

class HttpApi(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    
    @classmethod
    def RequestMethodGet(cls,url,port=None,header=None,cookies=None):
        parse =urlparse.urlparse(url)
        if(len(parse.query)==0):
            neturl = parse.path
        else:
            neturl = parse.path+"?"+parse.query
        
        http = MIGHttpMethodGet(neturl,parse.netloc)
        http.HttpMethodGet(header, cookies, port)
        return http.HttpGetContent()
    
    @classmethod
    def RequestMethodPost(cls,url,data,header=None,cookies=None):
        parse =urlparse.urlparse(url)
        neturl = parse.path
        http = MIGHttpMethodPost(neturl,parse.netloc)
        http.HttpMethodPost(data, header, cookies)
        return http.HttpGetContent()
        