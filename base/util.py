#!/usr/bin/python2.6  
# -*- coding: utf-8 -*-  
#encoding=utf-8

'''
Created on 2014年5月31日

@author: kerry
'''

import json
import uuid

def MIGGetResult(content):
    dic = eval(content)
    object =json.loads(content)
    if(object["status"]==1):
        if(dic.has_key("result")):
            content = object["result"]
        else:
            content = ""
        return 1,content
    else:
        content = ""
        return 0,content

def GetMac():
    mac=uuid.UUID(int = uuid.getnode()).hex[-12:] 
    return ":".join([mac[e:e+2] for e in range(0,11,2)])

        
    