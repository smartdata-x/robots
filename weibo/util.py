#!/usr/bin/python2.7  
# -*- coding: utf-8 -*-  
#encoding=utf-8

'''

@author: tangjl
'''
import ConfigParser 
 
def getServerInfo(ini = 'server_config.ini'):
    config = ConfigParser.ConfigParser()
    config.readfp(open(ini, 'rb'))
    ip = config.get('info', 'ip')  
    port = config.get('info', 'port')  
    return ip,port

def getWeiboLoginInfo(txt = 'weibo_info.txt'):
    result = []
    with open(txt, 'rb') as weibofile:
        for line in weibofile:
            line = line.rstrip( ) 
            result.append(list(map(str, line.split(','))))
        return result
        
    