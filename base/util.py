#!/usr/bin/python2.6  
# -*- coding: utf-8 -*-  
#encoding=utf-8

'''
Created on 2014年5月31日

@author: kerry
'''

import json

def MIGGetResult(content):
    object =json.loads(content)
    if(object["status"]==1):
        content = object["result"]
        return 1,content
    else:
        return 0
    