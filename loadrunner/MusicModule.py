#!/usr/bin/python 
# -*- coding: utf-8 -*-  
#encoding=utf-8
'''
Created on 2015年4月26日

@author: pro
'''
from pylib.threadpool import ThreadPool,NoResultsPending,makeRequests
from pub.ThreadMgr import ThreadMgr
from loadrunner.BaseModule import BaseModule
from base.miglog import miglog
from api.Entity import GetDimensions,GetCltSongs,SetCurrentSong,NearMusic
from api.MusicApi import MusicApi

class MusicModule(BaseModule):
    '''
    classdocs
    '''
    
    def __init__(self):
        '''
        Constructor
        '''
        self.uid = 10300
        self.token = "8b507cca826347a8cd5fd8a5a53c6b4d"
    
    def GetDimensions(self,data):
        dimensions = GetDimensions(self.uid,self.token)
        print MusicApi.GetDimensions(dimensions)
        result = round(4, 5)
        return result
    
    def GetCltSongs(self,data):
        cltsong = GetCltSongs(self.uid,self.token)
        print MusicApi.GetCltSongs(cltsong)
        result = round(4, 5)
        return result
    
    def GetNearMusic(self,data):
        nearmusic = NearMusic(self.uid,self.token)
        print MusicApi.GetNearMusic(nearmusic)
        result = round(4, 5)
        return result
    
    def GetNearUser(self,data):
        nearmusic = NearMusic(self.uid,self.token)
        nearmusic.latitude = 120.197
        nearmusic.longitude = 30.2624
        print MusicApi.GetNearUser(nearmusic)
        result = round(4, 5)
        return result
        
    def SetCurrentSong(self,data):
        current = SetCurrentSong(10302,"twrwerwr3243",0,9913,"chl",\
                 "孤单背影","陈慧娴",0,1)
        print MusicApi.SetCurrentSong(current)
        
        current1 = SetCurrentSong(10301,"twrwerwr3243",0,22424,"chl",\
                 "讲不出再见","谭咏麟",0,1)
        print MusicApi.SetCurrentSong(current1)
        
        current2 = SetCurrentSong(10300,"twrwerwr3243",0,35603,"chl",\
                 "不孤单","王杰",0,1)
        print MusicApi.SetCurrentSong(current2)
                
        current3 = SetCurrentSong(10299,"twrwerwr3243",0,52262,"chl",\
                 "倩女幽魂","张国荣",0,1)
        print MusicApi.SetCurrentSong(current3)
        '''   
        current4 = SetCurrentSong(10296,"twrwerwr3243",0,99877,"chl",\
                 "在路上","麦田守望者",0,1)
        print MusicApi.SetCurrentSong(current4)
            
        current5 = SetCurrentSong(10151,"twrwerwr3243",0,125009,"chl",\
                 "自助旅行","蔡淳佳",0,1)
        print MusicApi.SetCurrentSong(current5)
        
        current6 = SetCurrentSong(10294,"twrwerwr3243",0,211843,"chl",\
                 "偿还","王菲",0,1)
        print MusicApi.SetCurrentSong(current6)
        '''
        result = round(4,5)
        return result
        
        
        
        
class MusicScheduler(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    
        self.music_module = MusicModule()
        self.content =  [ 0 for i in range(5000)]
    
    def Start(self):
        #self.music_module.GetNearMusic(self.content)
        #ThreadMgr.CreateThreadPoolWork(self.content, 100, self.music_module.GetDimensions,\
         #self.music_module.EventStop, self.music_module.EventException)
        #ThreadMgr.CreateThreadPoolWork(self.content, 100, self.music_module.GetCltSongs,\
         #self.music_module.EventStop, self.music_module.EventException)
         ThreadMgr.CreateThreadPoolWork(self.content, 100, self.music_module.GetNearUser,\
         self.music_module.EventStop, self.music_module.EventException)
        