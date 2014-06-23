#!/usr/bin/python2.6  
# -*- coding: utf-8 -*-  
#encoding=utf-8
'''
Created on 2014年6月22日

@author: kerry
'''

from base.httpinterface import MigHttpInterFace
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
        data = "uid="+str(uid)+"&lastsong=0&cursong="+str(cursong)+"&mode="+"chl"+"&name="+"窦唯"+"&singer="+"无地自容"+"&state=0"+"&typeid="+str(typeid)
        miglog.log().debug(data)
        return MigHttpInterFace.RecordMusic(data)