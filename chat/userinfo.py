#!/usr/bin/python2.6  
# -*- coding: utf-8 -*-  
#encoding=utf-8

'''
Created on 2014年6月4日

@author: Administrator
'''

class UserInfo():
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.platform_id = 0
        self.uid = 0
        self.nicknumber = 0
        self.session = 0
        self.nickname = ""
        self.head_url = ""
        self.token = ""
        
    def set_platform_id(self,platform_id):
        self.platform_id = platform_id
    
    def get_platform_id(self):
        return self.platform_id
    
    def set_uid(self,uid):
        self.uid = uid
        
    def get_uid(self):
        return self.uid
    
    def set_nicknumber(self,nicknumber):
        self.nicknumber = nicknumber
        
    def get_nicknumber(self):
        return self.nicknumber
    
    def set_session(self,session):
        self.session = session
    
    def get_session(self):
        return self.session
    
    def set_nickname(self,nickname):
        self.nickname = nickname
    
    def get_nickname(self):
        return self.nickname
    
    def set_head_url(self,head_url):
        self.head_url = head_url
    
    def get_head_url(self):
        return self.head_url
    
    def set_token(self,token):
        self.token = token
    
    def get_token(self):
        return self.token
      
        