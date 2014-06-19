#!/usr/bin/python2.6  
# -*- coding: utf-8 -*-  
#encoding=utf-8
'''
Created on 2014年6月11日

@author: Administrator
'''
from base.http import MIGHttpMethodGet,MIGHttpMethodPost
import base.util as util
import json

class MigHttpInterFace(object):
    '''
    classdocs
    '''
    address = "/cgi-bin/"
    host = "112.124.49.59"


    def __init__(self):
        '''
        Constructor
        '''
    # 获取用户信息
    @classmethod 
    def GetRobotInfo(cls,index,count):
        url = cls.address+"getrobots.fcgi?from="+str(index)+"&count="+str(count)
        host =cls.host
        http = MIGHttpMethodGet(url,host)
        http.HttpMethodGet()
        result,content = util.MIGGetResult(http.HttpGetContent())
        if(result==1):
            return content
        else:
            print "GetResult Error"
    
    #赠送歌曲
    @classmethod
    def DoSendMusic(cls,senderId, receiverId,  msg):     
        url = cls.address + "presentsong.fcgi"
        host = cls.host
        http = MIGHttpMethodPost(url,host)
        data = {'uid':str(senderId),'touid':str(receiverId),'msg':msg}
        http.HttpMethodPost(data=data,urlcode=0)
        result,content =  util.MIGGetResult(http.HttpGetContent())
        if(result==1):
            return content
        else:
            print "GetResult Error"
            
    #打招呼
    @classmethod
    def DoSayHello(cls,senderId, receiverId, msg):
        url = cls.address+"sayhello.fcgi"
        host = cls.host
        http = MIGHttpMethodPost(url,host)
        data = {'uid':str(senderId),'touid':str(receiverId),'msg':msg}
        http.HttpMethodPost(data=data,urlcode=1)
        result,content =  util.MIGGetResult(http.HttpGetContent())
        if(result==1):
            return content
        else:
            print "GetResult Error"
        
    #添加新的歌曲
    @classmethod
    def AddNewMusic(cls,data):
        url = cls.address+"addnewmusic.fcgi"
        host = cls.host
        data ="content="+str(json.dumps(data))
        http = MIGHttpMethodPost(url,host)
        http.HttpMethodPost(data=data)
        result,content =  util.MIGGetResult(http.HttpGetContent())
        if(result==1):
            return content
        else:
            print "GetResult Error"
        
    #更新机器人头像
    @classmethod
    def UpdateRobotHead(cls,data):
        url = cls.address+"updaterobotpic.fcgi"
        host = cls.host
        post_data ="content="+data
        http = MIGHttpMethodPost(url,host)
        http.HttpMethodPost(data=post_data)
        return http.HttpGetContent()
    
    #获取发送邮件内容
    @classmethod
    def MailSubjectAndContent(cls):
        url = cls.address + "getspreadmail.fcgi"
        host = cls.host
        http = MIGHttpMethodGet(url,host)
        http.HttpMethodGet()
        result,content = util.MIGGetResult(http.HttpGetContent())
        if(result==1):
            return content
        else:
            print "GetResult Error"
        
    #获取发送者列表
    @classmethod
    def ParserToList(cls,index,count):
        url = cls.address + "getmailinfo.fcgi?from="+index+"count="+count
        host = cls.host
        http = MIGHttpMethodGet(url,host)
        http.HttpMethodGet()
        result,content = util.MIGGetResult(http.HttpGetContent())
        if(result==1):
            return content
        else:
            print "GetResult Error"
        
        
        
