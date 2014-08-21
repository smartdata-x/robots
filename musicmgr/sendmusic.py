#!/usr/bin/python2.6  
# -*- coding: utf-8 -*-  
#encoding=utf-8

'''
Created on 2014年6月10日

@author: archer
'''
from base.http import MIGHttpMethodPost
from base.httpinterface import MigHttpInterFace
from base.miglog import  miglog


class AutoSendMusicBase:
    def __init__(self):
        self.null = 0
        
class AutoSendMusic(AutoSendMusicBase):
    def __init__(self):
        AutoSendMusicBase.__init__(self)
        self.url = '/cgi-bin/presentsong.fcgi'
        #self.host = "42.121.14.108"
        self.host = "112.124.49.59"
        self.senderId = 10149
        self.msg = ''
        
        
        
    def DoSendMusic(self, senderId, receiverId, musicId, msg):
        #参数检查
        if(type(senderId) != type(1) 
           or type(receiverId) != type(1) 
           or type(musicId) != type(1) 
           or type(msg) != type('1')):
            print 'DoSendMusic Invalid Parameter'
            return False
        http = MIGHttpMethodPost(self.url, self.host)
        songs = ''
        
        if type(musicId) == type(1):
            songs = '{"songid":"' + str(musicId) + '","msg":"' + msg + '"}'
        elif type(musicId) == type([1,2]):
            for singleId in musicId:
                singleSong = '{"songid":"' + str(singleId) + '","msg":"' + msg + '"}'
                songs = songs + singleSong + ','
            
                #去掉最后一个逗号
            songs = songs[:-1]
        
        
        content = '{"song":[' + songs + ']}'
        
        #content = '{"song":[{"songid":"' + str(musicId) + '","msg":"' + msg + '"}]}'
        #data = 'uid=' + str(senderId) + '&touid=' + str(receiverId) + '&msg=' + content
        miglog.log().debug(content)
        
        print MigHttpInterFace.DoSendMusic(senderId, receiverId, content)
       
       
       
    #批量设置发送 
    def SetSenderId(self, senderId):
        #参数检查
        if type(senderId) != type(1):
            print 'SetSenderId Invalid Parameter'
            return False
            
        self.senderId = senderId
        
        
        
    def SetMessage(self, msg):
        #参数检查
        if type(msg) != type('1'):
            print 'SetMessage Invalid Parameter'
            return False
            
        self.msg = msg
        
        
        
    def DoSendMusicAll(self, receiverId, musicId):
        #参数检查
        if type(receiverId) != type(1) or type(musicId) != type(1):
            print 'DoSendMusicAll Invalid Parameter'
            return False
            
        self.DoSendMusic(senderId=self.senderId, receiverId=receiverId, musicId=musicId, msg=self.msg)
