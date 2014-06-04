#!/usr/bin/python2.6  
# -*- coding: utf-8 -*-  
#encoding=utf-8

'''
Created on 2014年6月5日

@author: kerry
'''
from chat import migprotocol
from userinfo import UserInfo

class ImMgr(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    def TextPrivateSend(self,userinfo,recv_user_id,content):
        text_private = migprotocol.TextChatPrivateSend()
        text_private.make_head(1100, 2, 0, 0)
        text_private.set_platform_id(userinfo.get_platform_id())
        text_private.set_send_user_id(userinfo.get_uid())
        text_private.set_recv_user_id(recv_user_id)
        text_private.set_session(userinfo.get_session())
        text_private.set_token(userinfo.get_token())
        text_private.set_content(content)
        return text_private.packstream()
    
    def TextPrivateRecv(self,data):
        text_prviate = migprotocol.TextChatPrivateRecv()
        text_prviate.unpackstream(data)
        print text_prviate.content
        