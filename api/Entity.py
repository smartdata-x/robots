#!/usr/bin/python 
# -*- coding: utf-8 -*-  
#encoding=utf-8
'''
Created on 2015年4月21日

@author: kerry
'''


class GetCltSongs(object):
    '''
    classdocs
    '''
    def __init__(self,uid,token):
        self.uid = uid
        self.token = token
        
    def dict(self):
        dict={}
        dict["uid"] = self.uid
        dict["token"] = self.token
        return dict

class NearMusic(GetCltSongs):
    def __init__(self,uid,token):
        GetCltSongs.__init__(self, uid, token)
        self.latitude = 0.0
        self.longitude = 0.0
        
    
    def dict(self):
        dict = {}
        dict["uid"] = self.uid
        dict["token"] = self.token
        if(self.latitude!=0.0):
            dict["latitude"] = self.latitude
        if(self.longitude!=0.0):
            dict["longitude"] = self.longitude
        
        return dict
    

class GetDimensions(object):
    '''
    classdocs
    '''

    def __init__(self,uid,token):
        self.uid = uid
        self.token = token
        self.moodid = 4
        self.moodindex = 0
        self.typeid = 1
        self.typeindex = 0
        self.sceneindex = 0
        self.sceneid = 5
        self.channelid = 6
        self.channelindex = 0
        self.num = 5
    
    def dict(self):
        dict = {}
        dict["uid"] = self.uid
        dict["token"] = self.token
        dict["moodid"] = self.moodid
        dict["moodindex"] = self.moodindex
        dict["typeid"] = self.typeid
        dict["typeindex"] =  self.typeindex
        dict["sceneindex"] = self.sceneindex
        dict["sceneid"] = self.sceneid
        dict["channelid"] = self.channelid
        dict["channelindex"] = self.channelindex
        dict["num"] = self.num
        return dict

class SetCurrentSong(object):
    '''
    classdocs
    '''
    
    def __init__(self,uid,token,lastsong,cursong,mode,\
                 name,singer,state,typeid):
        '''
        Constructor
        '''
        self.uid = uid
        self.token = token
        
        self.lastsong = lastsong
        self.cursong = cursong
        self.mode = mode
        self.name = name
        self.singer = singer
        self.state = state
        self.typeid = typeid
    
    def dict(self):
        dict = {}
        dict["uid"] = self.uid
        dict["token"] = self.token
        
        dict["lastsong"] = self.lastsong
        dict["cursong"] = self.cursong
        dict["mode"] = self.mode
        dict["name"] = self.name
        dict["singer"] = self.singer
        dict["state"] = self.state
        dict["typeid"] = self.typeid
        return dict

class ThirdLoginInfo(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.source = 0 #来源
        self.machine = 0 #机型
        self.nickname = ""
        self.sex = 0
        self.session = ""
        self.bithiday = ""
        self.location = ""
        self.head = ""
        self.imei =""
        
    def dict(self):
        dict = {}
        dict["source"] = self.source
        dict["machine"] = self.machine
        dict["nickname"] = self.nickname
        dict["sex"] = self.sex
        dict["session"] =self.session
        dict["birthday"] = self.bithiday
        dict["location"] = self.location
        dict["head"] = self.head
        dict["imei"] = self.imei
        return dict