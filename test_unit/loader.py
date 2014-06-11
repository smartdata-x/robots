#!/usr/bin/python2.6  
# -*- coding: utf-8 -*-  
#encoding=utf-8

import sys
'''
Created on 2014年5月28日

@author: kerry
'''

from base.http import MIGHttpMethodGet,MIGHttpMethodPost
from spidermusic.kowuspider import SpiderKuWo
from spidermusic.spidermusic import SpiderMusic
#from chat.netservice import MIGSchedulerClient
#from chat.chat_mgr import ChatMgr
from mail.autosender import AutoSendMail
<<<<<<< HEAD
from base.robotinfos import RobotInfoMgr
from multiprocessing import Process,Pool
from base.log import  miglogging
=======
#from base.robotinfos import RobotInfoMgr
from hallo.sayhello import AutoSayHello
#from chat.netservice import MIGSchedulerClient
#from chat.chat_mgr import ChatMgr
#from robotmgr.infomgr import RobotInfoMgr
#from mail.autosender import AutoSendMail
#from base.robotinfos import RobotInfoMgr
from sendmusic.sendmusic import AutoSendMusic

def TestHello():
    say = AutoSayHello()
    say.DoSayHello(10149, 10181, 'hahhaha,wo')
    
>>>>>>> 4e73c48acdf3429e6969a36141e5c2d2c434f663

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
    name = "小苹果"
    singer = "老男孩"
    spider = SpiderKuWo()
    album,album_pic,artist,rid,songname,star_pic,star_web,url =  spider.SpidertKuWoMusicInfo(name, singer)
    print url,album_pic
    
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
    send.DoSendMusic(10149, 10108, 241632, 'wochanfdheflldsagekkdgitleigtl')
    
    
def f(x):
    print x*x
    
def TestPool():
    pool = Pool(processes=4)
    result = pool.apply_async(f, [10])
    result = pool.apply_async(f, [10])
    result = pool.apply_async(f, [10])
    pool.close()
    pool.join()
    
if __name__ == '__main__':
    #reload(sys)
    #sys.setdefaultencoding('utf-8')
    #print sys.getdefaultencoding()
    #TestModuleHttp()
    #TestModuleSpiderKuWo()
    #TestSpiderMusic()
    #TestSocket()
<<<<<<< HEAD

    TestRobotChat()
    #asm = AutoSendMail()
    #asm.ASMDoStep()
    #TestRobotInfo()
    #TestPool()
    #asm = AutoSendMail()
    #asm.ASMDoSend()
=======
    #TestRobotInfoMgr()
    #TestRobotChat()
    #asm = AutoSendMail()
    #asm.ASMDoStep()
    #TestRobotInfo()
    #asm = AutoSendMail()
    #asm.ASMDoSend()
    TestHello()
    TestSendMusic()
>>>>>>> 4e73c48acdf3429e6969a36141e5c2d2c434f663
    

    
    
    