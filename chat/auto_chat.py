#!/usr/bin/python2.6  
# -*- coding: utf-8 -*-  
#encoding=utf-8

'''
Created on 2014年7月5日

@author: Administrator
'''


APP_KEY = '3226898525'  
APP_SECRET = 'aef4ebe03efeb3ee117f8764e0dfb701'  
CALL_BACK = 'https://api.weibo.com/oauth2/default.html'

from weibo import initclient
import time

class AutoChat(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.client = initclient.get_client(APP_KEY, APP_SECRET, CALL_BACK)
    
    def AutoChatContent(self,content):
        comments = self.client.request_xiaobing(content)
        if(len(comments)==0):
            comments = "[/84]"
        return comments
        