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
    name = "夜空中最闪亮的星"
    singer = "逃跑计划"
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
    
if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    print sys.getdefaultencoding()
    #TestModuleHttp()
    #TestModuleSpiderKuWo()
    TestSpiderMusic()
    

    
    
    