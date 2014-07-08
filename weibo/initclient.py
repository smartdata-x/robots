#!/usr/bin/python2.7  
# -*- coding: utf-8 -*-

import weibo   
import urllib  
import time  
import os  
  
  
class myAPIClient(weibo.APIClient):  
    ''' 
   myAPIClient类继承自weibo包中的APIClient类，对其进行了扩展。SDK中的APIClient类没有根据已授权的access_token获取授权详细信息的接口。另外，SDK中 
        的APIClient不能保存当前授权用户的uid，该继承类实现了这两个功能，使得用起来更加方便。 
    '''  
    def __init__(self,app_key,app_secret,redirect_uri=None,response_type='code',domain='api.weibo.com',version='2'):  
       weibo.APIClient.__init__(self,app_key,app_secret,redirect_uri,response_type='code',domain='api.weibo.com',version='2')  
       #保存当前授权用户的uid  
       self.uid=''
  
    def request_access_token_info(self,at):  
        ''' 
                该接口传入参数at为已经授权的access_token，函数将返回该access_token的详细信息，返回Json对象，与APIClient类的request_access_token类似。 
    '''  
        r = weibo._http_post('%s%s' % (self.auth_url, 'get_token_info'), access_token = at)  
        current = int(time.time())  
        expires = r.expire_in + current  
        remind_in = r.get('remind_in', None)  
        if remind_in:  
            rtime = int(remind_in) + current  
        #if rtime < expires:  
            #expires = rtime  
        return weibo.JsonDict(expires=expires, expires_in=expires, uid=r.get('uid', None))  
      
    def set_uid(self, uid):  
        self.uid = uid  
            
    '''
    @小冰
    '''
    def request_xiaobing(self,content):
        #读取获取用户发布的微博的ID,http://open.weibo.com/wiki/2/statuses/user_timeline/ids
        ids_return = self.statuses.user_timeline.ids.get(access_token=self.access_token,count='1')
        if 0 < len(ids_return.statuses) : 
                #评论一条微博,http://open.weibo.com/wiki/2/comments/create
                create_return = self.comments.create.post(access_token=self.access_token,comment='@小冰  '+content,id=ids_return.statuses)
                time.sleep(5)
                #我收到的评论列表,http://open.weibo.com/wiki/2/comments/to_me
                to_me_return = self.comments.to_me.get(access_token=self.access_token,since_id=create_return.id)
                for comments_return in to_me_return.comments :
                    if comments_return.reply_comment.id == create_return.id : 
                        #批量删除评论,http://open.weibo.com/wiki/2/comments/destroy_batch
                        self.comments.destroy_batch.post(access_token=self.access_token,cids=create_return.id)
                        self.comments.destroy_batch.post(access_token=self.access_token,cids=comments_return.id)
                        return comments_return.text[comments_return.text.find(':')+1:]
        return ''
  
TOKEN_FILE = 'token-record.log'  
def load_tokens(filename=TOKEN_FILE):  
    acc_tk_list = []  
    try:  
        filepath = os.path.join(os.path.dirname(__file__), filename)  
        f = open(filepath)  
        acc_tk_list.append(f.readline().strip())  
        f.close()  
        print '===> Get the access_token from file token-record.log : ', acc_tk_list[0]  
    except IOError:  
        print '===> File token-record.log does not exist.'  
    return acc_tk_list  
  
'''
从文件中读取授权信息
'''
def dump_tokens(tk, filename=TOKEN_FILE):  
    try:  
        filepath = os.path.join(os.path.dirname(__file__), filename)  
        f = open(filename, 'a')  
        f.write(tk)  
        f.write('\n')  
    except IOError:  
        print '===> File token-record.log does not exist.'  
    f.close()  
    print '===> The new access_token has been written to file token-record.log.'  
  
  
def get_client(appkey, appsecret, callback):  
    client = myAPIClient(appkey, appsecret, callback)  
    at_list = load_tokens()  
    if at_list:  
        access_token = at_list[-1]  
        r = client.request_access_token_info(access_token)  
        expires_in = r.expires_in  
        print "===> The access_token's expires_in : %f" % expires_in  
                #授权access_token过期  
        if r.expires_in <= 0:  
            return None  
        client.set_uid(r.uid)  
        #client.request_comment_create('3221164604', 'good!', '3689057571623924')
    else:  
        auth_url = client.get_authorize_url()  
        print '===> auth_url : ' + auth_url   
        print '''===> Note! The access_token is not available, you should be authorized again. Please open the url above in your browser,  
then you will get a returned url with the code field. Input the code in the follow step.'''  
        code = raw_input('===> input the retured code : ')  
        r = client.request_access_token(code)  
        access_token = r.access_token  
        expires_in = r.expires_in  
        print '===> the new access_token is : ', access_token  
        dump_tokens(access_token)  
    client.set_access_token(access_token, expires_in)  
    client.set_uid(r.uid)  
    return client  

