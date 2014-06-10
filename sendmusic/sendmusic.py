#!/usr/bin/python2.6  
# -*- coding: utf-8 -*-  
#encoding=utf-8

'''
Created on 2014年6月10日

@author: archer
'''
from base.http import MIGHttpMethodPost

class AutoSendMusicBase:
    def __init__(self):
        self.null = 0
        
class AutoSendMusic(AutoSendMusicBase):
    def __init__(self):
        AutoSendMusicBase.__init__(self)
        self.url = 'http://112.124.49.59/cgi-bin/presentsong.fcgi'
        self.host = '112.124.49.59'
        self.senderId = 10149
        self.msg = ''
        
    def DoSendMusic(self, senderId, receiverId, musicId, msg):
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
        data = 'uid=' + str(senderId) + '&touid=' + str(receiverId) + '&msg=' + content
        print data
    
        http.HttpMethodPost(data=data,urlcode=0)
        print http.HttpGetContent()
       
    #批量设置发送 
    def SetSenderId(self, senderId):
        self.senderId = senderId
        
    def SetMessage(self, msg):
        self.msg = msg
        
    def DoSendMusicAll(self, receiverId, musicId):
        self.DoSendMusic(senderId=self.senderId, receiverId=receiverId, musicId=musicId, msg=self.msg)
