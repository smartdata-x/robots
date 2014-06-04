#!/usr/bin/python2.6  
# -*- coding: utf-8 -*-  
#encoding=utf-8

'''
Created on 2014年6月4日

@author: Administrator
'''
from chat import migprotocol
class FileMgr(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    def SendSoundFile(self,userinfo):
        send_sound_file = migprotocol.MutilSoundSend()
        send_sound_file.make_head(2100,2, 0, 0)
        send_sound_file.set_platform_id(10000)
        send_sound_file.set_multi_id(10150)
        send_sound_file.set_multi_type(3)
        send_sound_file.set_send_user_id(userinfo.get_uid())
        send_sound_file.set_session(10150)
        send_sound_file.set_token(userinfo.get_token())
        send_sound_file.set_sound_path("/var/www/1.mp3")
        return send_sound_file.packstream()
        