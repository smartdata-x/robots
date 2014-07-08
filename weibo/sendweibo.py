#!/usr/bin/python2.7  
# -*- coding: utf-8 -*-

'''
Created on 2014年6月4日

@author: along
'''

'''
import weibo

APP_KEY = '3226898525'  
APP_SECRET = 'aef4ebe03efeb3ee117f8764e0dfb701'  
CALL_BACK = 'https://api.weibo.com/oauth2/default.html'  

def run():  
        #weibo模块的APIClient是进行授权、API操作的类，先定义一个该类对象，传入参数为APP_KEY, APP_SECRET, CALL_BACK  
    client = weibo.APIClient(APP_KEY, APP_SECRET, CALL_BACK)  
        #获取该应用（APP_KEY是唯一的）提供给用户进行授权的url  
    auth_url = client.get_authorize_url()  
    #打印出用户进行授权的url，将该url拷贝到浏览器中，服务器将会返回一个url，该url中包含一个code字段（如图1所示）  
    print "auth_url : " + auth_url  
    #输入该code值（如图2所示）  
    code = raw_input("input the retured code : ")  
    #通过该code获取access_token，r是返回的授权结果，具体参数参考官方文档：  
    # http://open.weibo.com/wiki/Oauth2/access_token  
    r = client.request_access_token(code)  
        #将access_token和expire_in设置到client对象  
    client.set_access_token(r.access_token, r.expires_in)  
  
    #以上步骤就是授权的过程，现在的client就可以随意调用接口进行微博操作了，下面的代码就是用用户输入的内容发一条新微博  
  
    while True:  
        print "Ready! Do you want to send a new weibo?(y/n)"  
        choice = raw_input()  
        if choice == 'y' or choice == 'Y':  
            content = raw_input('input the your new weibo content : ')  
            if content:  
                                #调用接口发一条新微薄，status参数就是微博内容  
                client.statuses.update.post(status=content)  
                print "Send succesfully!"  
                break;  
            else:  
                print "Error! Empty content!"  
        if choice == 'n' or choice == 'N':  
            break  
    
    
if __name__ == "__main__":
    run()
'''

import initclient
import time


APP_KEY = '3226898525'  
APP_SECRET = 'aef4ebe03efeb3ee117f8764e0dfb701'  
CALL_BACK = 'https://api.weibo.com/oauth2/default.html'  
'''
APP_KEY = '4082577001'  
APP_SECRET = 'ffceb9ce49142b68f18d84fa216ea350'  
CALL_BACK = 'http://42.121.14.108/3rdauth/sinaweibo/callback.php'  
'''


def run():  
        #调用initclietn模块创建授权的client对象  
    client = initclient.get_client(APP_KEY, APP_SECRET, CALL_BACK)  
    if not client:  
                return  
  
        #根据用户输入内容发微博  
    while True:  
        '''
        to_me_return = client.comments.to_me.get(access_token=client.access_token,since_id='3730061511641986')
        contents = "好热啊！"
        for comments_return in to_me_return.comments :
            if comments_return.reply_comment.id == 3730061511641986 : 
                print comments_return.text
        '''
        #ids_return = client.statuses.user_timeline.ids.get(access_token=client.access_token,count='1')
        print "Ready! Do you want to send a new weibo?(y/n)"  
        choice = raw_input()  
        if choice == 'y' or choice == 'Y':  
            content = raw_input('input the your new weibo content : ')  
            if content:  
                #create_return = client.comments.create.post(access_token=client.access_token,comment='@小冰  '+content,id=ids_return.statuses)
                comments = client.request_xiaobing(content)
                if comments :
                    print comments
                print "Send succesfully!"
                #time.sleep(10)
                #to_me_return = client.comments.to_me.get(access_token=client.access_token,since_id=create_return.id)
                #print to_me_return.text
                break;  
            else:  
                print "Error! Empty content!"  
        if choice == 'n' or choice == 'N':  
            break  
  
if __name__ == "__main__":  
    run()
