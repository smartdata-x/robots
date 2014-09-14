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
        self.token = ""
        #self.autochat = AutoChat()
        self.weibo = weiboService.getWeibo(self.reply)
        #self.transport = transport
        #self.callback = callback
        
    def reply(self,clientid, replymsg):
        #self.TextPrivateSend(userinfo, clientid, replymsg)
        if(len(replymsg)==0):
            replymsg = "[/84]"
        #self.transport.write(self.TextPrvateSendV2(clientid, replymsg))
        self.callback(self.TextPrvateSendV2(clientid, replymsg))
        
    def TextPrvateSendV2(self,recv_user_id,content):
        miglog.log().debug("=====================")
        miglog.log().debug(self.platform_id)
        miglog.log().debug(self.uid)
        miglog.log().debug(recv_user_id)
        miglog.log().debug(self.session)
        miglog.log().debug(self.token)
        miglog.log().debug(content)
        miglog.log().debug("=====================")
        text_private = migprotocol.TextChatPrivateSend()
        text_private.make_head(1100, 2, 0, 0)
        text_private.set_platform_id(self.platform_id)
        text_private.set_send_user_id(self.uid)
        text_private.set_recv_user_id(int(recv_user_id))
        text_private.set_session(self.session)
        text_private.set_token(self.token)
        text_private.set_content(content)
        return text_private.packstream()
        
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
    

    
    def TextPrivateRecv(self,data,callback,userinfo):
        #self.callback = callback
        text_prviate = migprotocol.TextChatPrivateRecv()
        text_prviate.unpackstream(data)
        self.platform_id = text_prviate.platform_id
        self.session = userinfo.get_session()
        self.token = userinfo.get_token()
        self.uid = userinfo.get_uid()
        miglog.log().debug("content %s",str(text_prviate.get_content()))
        self.weibo.requestXiaobing(str(text_prviate.send_user_id),str(text_prviate.get_content()))
        self.callback = callback
        #comment = self.autochat.AutoChatContent(text_prviate.content)
        #print comment
        #return self.TextPrivateSend(userinfo, text_prviate.get_send_user_id(), comment)
        #print text_prviate.content
        