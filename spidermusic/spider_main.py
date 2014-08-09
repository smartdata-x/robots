#!/usr/bin/python2.6  
# -*- coding: utf-8 -*-  
#encoding=utf-8

'''
Created on 2014年7月27日

@author: kerry
'''
import platform
import os
import sys
import time
from base.httpinterface import MigHttpInterFace
from kowuspider import SpiderKuWo
from spidermusic import SpiderMusic

def ProcessVailedUrlMusic():
    infos = [0 for i in range(0)];
    content = MigHttpInterFace.GetVailedUrlMusic()
    if(content=="Error"):
        return
    for element in content:
        info = {}
        print element["singer"]
        print element["id"]
        print element["name"]
        spider = SpiderKuWo()
        album,album_pic,artist,rid,songname,star_pic,star_web,url =  spider.SpidertKuWoMusicInfo(element["name"], element["singer"])
        print url
        print album_pic
        info["id"] = element["id"]
        info["url"] = url
        infos.append(info)
    MigHttpInterFace.UpdateMusicUrl(infos)

def ProcessAddNewMusic():
    spider = SpiderMusic()
    if(spider.GetNewMuisc()):
        spider.GetMuiscInfos()
        spider.PostNewMusicInfo()
    
def time_exec(inc = 10):
    while True:
        ProcessVailedUrlMusic()
        ProcessAddNewMusic()
        time.sleep(inc)
    
    
    
if __name__ == '__main__':
    print os.name
    sysstr = platform.system()
    if(platform.system()=="Darwin"):
        reload(sys)
        sys.setdefaultencoding('utf-8')
    time_exec()