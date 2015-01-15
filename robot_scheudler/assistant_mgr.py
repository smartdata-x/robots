#!/usr/bin/python2.6  
# -*- coding: utf-8 -*-  
#encoding=utf-8
'''
Created on 2014年7月1日

@author: kerry
'''
from robot_scheudler import robot_protocol
from chat import migprotocol
from base.miglog import miglog
from musicmgr.sendmusic import AutoSendMusic
from robot_scheudler.singleton_config import SingletonConfig
from socket import *

class AssistantMgr(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.uid = 0
        
    def UnpackHead(self,data):
        packet_head = robot_protocol.PacketHead()
        return  packet_head.unpackhead(data)
        
    def AssistantLogin(self,platform_id,uid,nickname):
        self.platformid = platform_id
        self.uid = uid
        self.nickname = nickname
        assistant_login =  robot_protocol.AssistantLogin()
        assistant_login.make_head(2101, 1, 0, 0)
        assistant_login.set_platform_id(platform_id)
        assistant_login.set_uid(uid)
        return assistant_login.packstream()
    
    def NoticeChatLuckGift(self,data):
        plat_name = ""
        prize_name = ""
        luck_gift = robot_protocol.NoticeGiftLuck()
        luck_gift.unpackstream(data)
        miglog.log().debug("platform %d, uid %d plat %d prize %d",luck_gift.platform_id,luck_gift.uid,luck_gift.share_plat,luck_gift.prize)
        ##组织文字
        if(luck_gift.share_plat==1):
            plat_name = "新浪微博"
        elif(luck_gift.share_plat==2):
            plat_name = "QQ空间"
        elif(luck_gift.share_plat==3):
            plat_name = "朋友圈"
        
        if(luck_gift.prize==1):
            prize_name = "一等奖"
        elif(luck_gift.prize==2):
            prize_name = "二等奖"
        elif(luck_gift.prize==3):
            prize_name = "三等奖"
            
        content = "恭喜你在"+plat_name+"分享歌曲"+str(luck_gift.artist[0:luck_gift.artist.index('\0')])+ str(luck_gift.song[0:luck_gift.song.index('\0')])+"）获得"+prize_name
        miglog.log().debug(content)
        #发送给聊天服务器
        sock = socket(AF_INET, SOCK_STREAM)  
        sock.connect((SingletonConfig().chathost,SingletonConfig.chatport))
        text_private = migprotocol.TextChatPrivateSend()
        text_private.make_head(1100, 2, 0, 0)
        text_private.set_platform_id(10000)
        text_private.set_send_user_id(10000)
        text_private.set_recv_user_id(luck_gift.uid)
        text_private.set_session(0)
        text_private.set_token("userinfo.get_token()")
        text_private.set_content(content)
        messlen = sock.send(text_private.packstream())
        sock.close() 
        
    def NoticeAssistantHandlse(self,data):
        handlse_song = robot_protocol.NoticeAssistantHandlseSong()
        handlse_song.unpackstream(data)
        #赠送给用户
        handlselist =[ 0 for i in range(0)]
        handlselist = handlse_song.gethandlselist()
        if(len(handlselist)>0):
            for robot in handlselist:
                send_music = AutoSendMusic();
                send_music.DoSendMusic(self.uid,robot.get_uid(),robot.get_songid(), robot.get_message().encode("UTF-8")  )
                
                
        
assistant_mgr = AssistantMgr()