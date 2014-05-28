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
    reload(sys)
    sys.setdefaultencoding('utf-8')
    print sys.getdefaultencoding()
    url = "http://wap.tyread.com/baoyueInfoListAction.action?monthProductId=23413150"
    host = "wap.tyread.com"
    http = MIGHttpResponse(url,host)
    http.HttpMethodGet()
    http.HttpGetContent()
    