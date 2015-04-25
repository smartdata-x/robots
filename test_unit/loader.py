#!/usr/bin/python2.6  
# -*- coding: utf-8 -*-  
#encoding=utf-8

import sys
'''
Created on 2014年5月28日

@author: kerry
'''

import platform
import os
from base.http import MIGHttpMethodGet,MIGHttpMethodPost
from spidermusic.kowuspider import SpiderKuWo
#from spidermusic.spidermusic import SpiderMusic
#from chat.netservice import MIGSchedulerClient
#from chat.chat_mgr import ChatMgr
#from mail.autosender import AutoSendMail

#from base.robotinfos import RobotInfoMgr
from multiprocessing import Process,Pool
from base.miglog import  miglog

#from base.robotinfos import RobotInfoMgr
#from hallo.sayhello import AutoSayHello
#from chat.netservice import MIGSchedulerClient
#from chat.chat_mgr import ChatMgr
#from robotmgr.infomgr import RobotInfoMgr
#from mail.autosender import AutoSendMail
#from base.robotinfos import RobotInfoMgr
#from chat.netservice import MIGSchedulerClient
#from musicmgr.sendmusic import AutoSendMusic
#from musicmgr.recordmusic import RecordMusic
#from robot_scheudler.robot_netservice import MIGRobotInitialScheduler
from loadrunner.Scheduler import LoaderRunnerScheduler
import base.util

def TestHello():
    say = AutoSayHello()
    say.DoSayHello(10149, 10181, 'hahhaha,wo')
    

def TestRecordMusic():
    uid = 10000166
    cursong = 211845
    mode = "chl"
    name = "翅膀"
    singer = "垃圾场"
    state = 0
    typeid = 1
    record_music = RecordMusic()
    record_music.DoRecordMusic(uid,cursong,mode,name,singer,state,typeid)
    
def TestModuleHttp():
    url = "http://wap.tyread.com/baoyueInfoListAction.action?monthProductId=23413150"
    host = "wap.tyread.com"
    headers = {
    "accept":"text/vnd.wap.wml, image/gif, image/png, image/jpg, image/jpeg, image/vnd.wap.wbmp, */*",
    "User-Agent":"Mozilla/5.0 (Linux; U; Android 2.3.3; zh-cn; HTC_DesireS_S510e Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Accept-Encoding":"gzip, deflate",
    "X-Up-Calling-Line-ID":"13388128872",
    "HTTP_X_UP_CALLING_LINE_ID":"13388128872",
    "Referer":"http://wap.tyread.com/goPreBuySubmit.action?monthProductId=16935860&chargeMode=4&qdid=22301701"
    }
    http = MIGHttpMethodGet(url,host)
    http.HttpMethodGet(header = headers,cookies = "qdid=11000")
    print http.HttpGetContent()


    url = "http://118.244.206.105/cgi-bin/paywapread.fcgi"
    data = {'phonenum':"13388128872",'platform':'10001'}
    host = "118.244.206.105"
    
    http = MIGHttpMethodPost(url,host)
    http.HttpMethodPost(data=data,flag=1)
    print http.HttpGetContent()
    
def TestModuleSpiderKuWo():
    name = "小镇姑娘原版伴奏"
    singer = ""
    spider = SpiderKuWo()
    album,album_pic,artist,rid,songname,star_pic,star_web,url =  spider.SpidertKuWoMusicInfo(name, singer)
    print url,album_pic
    
def TestModuleSpiderLyric():
    name = "匆匆那年"
    singer = "王菲"
    spider = SpiderKuWo()
    res =  spider.SpiderKuwoLyricInfo(name, singer)
    #过滤字符
    
    
def TestSpiderMusic():
    url = "http://112.124.49.59/cgi-bin/getnewmusic.fcgi"
    host = "112.124.49.59"
    spider = SpiderMusic()
    if(spider.GetNewMuisc(url,host)):
        spider.GetMuiscInfos()
    spider.PostNewMusicInfo()
    
    
def TestRobotChat():
    robots_schedule = ChatMgr()
    robots_schedule.ChatRobotSatrt()
    
    
def TestProcess():
    uid = 10000013
    client = MIGSchedulerClient()
    token ='414c1edda11bfec34d63b99deada4235'
    client.set_platform_id(10000)
    client.set_token(token)
    client.set_uid(uid)
    client.set_oppid(10108)
    client.set_oppo_type(1)
    client.Connection("112.124.49.59",17000)
    miglog.log().debug("11111111111111111111")
    client.start_run()
    
#继承
def TestSocket():
    client = MIGSchedulerClient()
    uid = 10149213
    platform = 10000
    token ='414c1edda11bfec34d63b99deada4235'
    client.set_platform_id(platform)
    client.set_token(token)
    client.set_uid(uid)
    client.set_oppid(10148)
    client.set_oppo_type(1)
    client.Connection("112.124.49.59",17000)
    client.start_run()

def TestRobotInfoMgr():
    mgr = RobotInfoMgr()
    mgr.UpdateUserHeadUrl()
    
def TestSendMusic():
    send = AutoSendMusic();
    send.DoSendMusic(10000, 10108, 241632, '一个33°晴朗的白天的天气,助理小哟为你带来一首梁静茹的暖暖.(位于浙江省杭州市余杭区高教路')
    
    
def f(x):
    print x*x
    
def TestRobotMgrV():
    robot_client = MIGRobotInitialScheduler()
    robot_client.set_platform_id(10000)
    robot_client.set_robot_id(100003)
    robot_client.set_uid(10108)
    robot_client.Connection("112.124.49.59", 19008)
    robot_client.start_run()
    
    
def TestPool():
    pool = Pool(processes=4)
    result = pool.apply_async(f, [10])
    result = pool.apply_async(f, [10])
    result = pool.apply_async(f, [10])
    pool.close()
    pool.join()
    
def TestLoadRunner():
    runner =  LoaderRunnerScheduler()
    runner.StartUser()

    
if __name__ == '__main__':
    print os.name
    print base.util.GetMac()
    sysstr = platform.system()
    if(platform.system()=="Darwin"):
        reload(sys)
        sys.setdefaultencoding('utf-8')
    #TestSendMusic()
    #print sys.getdefaultencoding()
    #TestModuleSpiderLyric()
    #TestModuleHttp()
    #TestModuleSpiderKuWo()
    #TestSpiderMusic()
    #TestSocket()
    #TestRobotMgrV()
    #TestProcess()
    #asm = AutoSendMail()
    #asm.ASMDoStep()
     #TestRobotInfo()
    #TestPool()
    #asm = AutoSendMail()
    #asm.ASMDoSend()
    #TestRobotInfoMgr()
    #TestRobotChat()
    #asm = AutoSendMail()
    #asm.ASMDoStep()
    #TestRobotInfo()
    #asm = AutoSendMail()
    #asm.ASMDoSend()
    #TestHello()
    #TestSendMusic()
    #TestRecordMusic()
    
    TestLoadRunner()
    

    
    
    