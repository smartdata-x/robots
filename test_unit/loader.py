#!/usr/bin/python2.6  
# -*- coding: utf-8 -*-  
#encoding=utf-8

import sys
'''
Created on 2014年5月28日

@author: kerry
'''

from base.http import MIGHttpResponse

if __name__ == '__main__':
    print sys.getdefaultencoding()
    url = "http://www.baidu.com"
    host = "www.baidu.com"
    http = MIGHttpResponse(url,host)
    http.HttpMethodGet()
    print http.HttpGetContent()