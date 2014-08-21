#!/usr/bin/python2.6  
# -*- coding: utf-8 -*-  
#encoding=utf-8

'''
Created on 2014年5月29日

@author: kerry
'''

import urllib
import json
from base.http import MIGHttpMethodGet,MIGHttpMethodPost


class SpiderKuWo():
    
    def __init__(self):
        self.album = ""
        self.album_pic = ""
        self.artist = ""
        self.rid = ""
        self.songname = ""
        self.star_pic = ""
        self.star_web = ""
        self.url = ""
    
    def __ResloverMP3Url(self,string):
        domain = "kuwo.cn"
        path = "resource"
        str_len =  len(string)
        pos = string.find(domain)
        host = string[0:pos+len(domain)]
        sub_str = string[pos+7:str_len]
        str_len = len(sub_str)
        pos = sub_str.find(path)
        resource = sub_str[pos+len(path):str_len]
        mp3_url = host+"/resource"+resource;
        return mp3_url
    
    def __ResloverStringMusicInfo(self,string):
        index = 0
        pos = string.find(',')
        while(pos!=-1):
            content_len = len(string)
            sub_message = string[0:pos]
            temp_content = string[pos+1:content_len]
            if index == 0:
                self.artist = sub_message
            elif index == 1:
                self.star_pic = sub_message
            elif index == 2:
                self.star_web = sub_message
            elif index == 4:
                self.album = sub_message
                self.album_pic = temp_content
            string = temp_content
            pos = temp_content.find(',')
            index = index + 1

    def __ResloverJsonBaseInfo(self,string):
        try:
            object = json.loads(string.replace('\'','"'))
            #print object
            self.rid = object["abslist"][0]["MUSICRID"]
            self.songname = object["abslist"][0]["SONGNAME"]
            self.artist = object["abslist"][0]["ARTIST"]
            self.album = object["abslist"][0]["ALBUM"]
        except:
            self.rid = {}
            self.songname = {}
            self.artist = {}
            self.album = {}
        finally:
            pass
            #print self.rid,self.songname,self.artist,self.album
        
    def GetKuWoMusicUrl(self):
        if(len(self.rid)==0):
            return
        url = "http://antiserver.kuwo.cn/anti.s?format=mp3&type=convert_url&response=url&rid="+self.rid
        host = "antiserver.kuwo.cn"
        http = MIGHttpMethodGet(url,host)
        http.HttpMethodGet()
        self.url = self.__ResloverMP3Url(http.HttpGetContent())
         
    def GetKuWoMusicInfo(self):
        url = "http://player.kuwo.cn/webmusic/sj/dtflagdate?flag=6&rid="+str(self.rid)
        host = "player.kuwo.cn"
        http = MIGHttpMethodGet(url,host)
        http.HttpMethodGet()
        self.__ResloverStringMusicInfo(http.HttpGetContent())
        
    def GetKuWoBaseInfo(self,name,singer):
        key = name+" "+singer
        key = key.decode('utf-8').encode('utf-8')
        key = urllib.quote(key)
        url = "http://search.kuwo.cn/r.s?all="+key+"&ft=music&newsearch=1&itemset=web_2013&client=kt&cluster=0&pn=0&rn=12&rformat=json&encoding=utf8"
        host = "search.kuwo.cn"
        http = MIGHttpMethodGet(url,host)
        http.HttpMethodGet()
        self.__ResloverJsonBaseInfo(http.HttpGetContent())
    
    def SpidertKuWoMusicInfo(self,name,singer):
        self.GetKuWoBaseInfo(name, singer)
        self.GetKuWoMusicInfo()
        self.GetKuWoMusicUrl()
        return self.album,self.album_pic,self.artist,self.rid,self.songname,self.star_pic,self.star_web,self.url
    
    def GetKuWoLyricInfo(self,rid):
        url = "http://www.kuwo.cn/geci/l_"+rid
        host = "www.kuwo.cn"
        http = MIGHttpMethodGet(url,host)
        http.HttpMethodGet()
        return http.HttpGetContent()
        
        
    def ResolveContent(self,content):
        start_flag = "<div id=\"lrc_yes\" class=\"lrc\">"
        end_flag = "</div>"
        start_pos = content.find(start_flag)
        if(start_pos==-1):
            return 0,""
        sub_content = content[start_pos+len(start_flag):len(content)]
        end_pos = sub_content.find(end_flag)
        return 1,sub_content[0:end_pos]
        
    def SpiderKuwoLyricInfo(self,name,singer):
        self.GetKuWoBaseInfo(name, singer)
        if(len(self.rid)==0):
            return ""
        start_pos = self.rid.find("_")
        if(start_pos==0):
            return ""
        rid = self.rid[start_pos+1:len(self.rid)]
        #print self.GetKuWoLyricInfo(rid)
        #print kuwolyric_parser.content
        result,cotent = self.ResolveContent(self.GetKuWoLyricInfo(rid))
        if(result==0):
            return ""
        
        return cotent.strip('\n').strip().replace('\'', '\\\'').replace('<br>','')