#!/usr/bin/python2.6  
# -*- coding: utf-8 -*-  
#encoding=utf-8
'''
Created on 2014年6月21日

@author: kerry
'''
from robot_scheudler import robot_protocol
from musicmgr.sendmusic import AutoSendMusic
from musicmgr.recordmusic import RecordMusic

class RobotSongMgr(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    def OnRobotHandselSong(self,data):
        handsel_song = robot_protocol.NoticeRobotHandselSong()
        handsel_song.unpackstream(data)
        #赠送歌曲
        send_music = AutoSendMusic();
        send_music.DoSendMusic(handsel_song.get_robot_id(), handsel_song.get_uid(), handsel_song.get_song_id(), "121313")
    
    def OnRobotListenSong(self,robotuid,data):
        listen_song = robot_protocol.NoticeUserRobotListenSong()
        listen_song.unpackstream(data)
        #添加歌曲记录
        record_music = RecordMusic()
        record_music.DoRecordMusic(robotuid, listen_song.get_song_id(), listen_song.get_mode(),listen_song.get_name(), 
                                   listen_song.get_singer(), 0, listen_song.get_type_id())
        
        
robot_song_mgr = RobotSongMgr()