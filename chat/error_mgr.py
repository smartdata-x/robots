#!/usr/bin/python2.6  
# -*- coding: utf-8 -*-  
#encoding=utf-8


'''
Created on 2014年6月6日

@author: kerry
'''

from chat import migprotocol
from userinfo import UserInfo

class ErrorMgr(object):
        

    def __init__(self):
        '''
        Constructor
        '''
    def ErrorMsg(self,data):
        errpr_msg = migprotocol.ChatFailed()
        errpr_msg.unpackstream(data)
        return errpr_msg.get_error()
        