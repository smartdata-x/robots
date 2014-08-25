#!/usr/bin/python2.7  
# -*- coding: utf-8 -*-

import weiboService

def reply(clientid, replymsg):
    print clientid
    print replymsg

def run():  
        #调用initclietn模块创建授权的client对象  
    weibo = weiboService.getWeibo(reply)  
    weibo.requestXiaobing('11945', '来点新鲜的玩意儿吧')
    weibo.requestXiaobing('11324', '糟糕')
  
if __name__ == "__main__":  
    run()
