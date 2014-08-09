#!/usr/bin/python2.6  
# -*- coding: utf-8 -*-  
#encoding=utf-8

'''
Created on 2014年6月5日

@author: kerry
'''
from chat import migprotocol
from userinfo import UserInfo
from base.miglog import miglog
#from chat.auto_chat import AutoChat
import weibo.weiboService as weiboService

class ImMgr(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.platform_id = 0
        self.uid = 0
        self.oppsionid = 0
        self.session = 0
        #self.autochat = AutoChat()
        self.weibo = weiboService.getWeibo(self.reply)
        
    def reply(self,content, replymsg):
        print "+++++++++"
        print content
        print replymsg
        print "========"
        #self.TextPrivateSend(userinfo, text_prviate.get_send_user_id(), replymsg)
        
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
        miglog.log().debug("content %s",str(text_prviate.get_content()))
        self.weibo.requestXiaobing(text_prviate.content)
        #comment = self.autochat.AutoChatContent(text_prviate.content)
        #print comment
        #return self.TextPrivateSend(userinfo, text_prviate.get_send_user_id(), comment)
        #print text_prviate.content
        