#!/usr/bin/python2.6  
# -*- coding: utf-8 -*-  
#encoding=utf-8
'''
Created on 2014年6月22日

@author: kerry
'''

from api.Entity import SetCurrentSong
from api.MusicApi import MusicApi
from base.miglog import miglog

class RecordMusic(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    def DoRecordMusic(self,uid,cursong,mode,name,singer,state,typeid):
        current = SetCurrentSong(uid,"68474fc9c875459bf8c074b004cdd10a",0,cursong,mode,\
                 name,singer,0,int(typeid))
        return MusicApi.SetCurrentSong(current)