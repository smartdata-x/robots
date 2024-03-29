#!/usr/bin/python2.6  
# -*- coding: utf-8 -*-  
#encoding=utf-8


'''
Created on 2014年5月31日

@author: kerry
'''
from kowuspider import SpiderKuWo
from base.http import MIGHttpMethodGet,MIGHttpMethodPost
import base.util as util
import json
import base64

class SpiderMusic():
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.spider = SpiderKuWo()
        self.infos = [0 for i in range(0)]
    
        
    def GetNewMuisc(self):
        #http = MIGHttpMethodGet(url,host)
        #http.HttpMethodGet()
        #print http.HttpGetContent()
        #result,self.content = util.MIGGetResult(http.HttpGetContent())
        self.content = MigHttpInterFace.GetNewMusic()
        if(self.content=="Error"):
            return 0
        return 1
    
    def GetMuiscInfos(self):
        
        for element in self.content:
            album,album_pic,artist,rid,songname,star_pic,star_web,url = self.spider.SpidertKuWoMusicInfo(element["name"],element["singer"])
            info = {}
            info["id"] = element["id"]
            info["album"] = base64.b64encode(album)
            info["pic"] = album_pic
            info["artist"] = base64.b64encode(artist)
            info["name"] = base64.b64encode(songname)
            info["pubtime"] = "0"
            info["url"] = url
            #data =  json.dumps(info)
            self.infos.append(info)
            
    def PostNewMusicInfo(self):
        MigHttpInterFace.AddNewMusic(self.infos)
        
        