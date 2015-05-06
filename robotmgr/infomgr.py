#!/usr/bin/python2.6  
# -*- coding: utf-8 -*-  
#encoding=utf-8
'''
Created on 2014年6月9日

@author: kerry
'''
from base.http import MIGHttpMethodGet,MIGHttpMethodPost
import base.util as util
import json
from xml.etree import ElementTree

class RobotInfoMgr(object):
    '''
    classdocs
    '''
    '''
    def print_node(self,node):
        print "============================"
        print "node.attrib:%s" % node.attrib
        print "node.tag:%s" % node.tag
        print "node.text:%s" % node.text
      '''          

    def __init__(self):
        '''
        Constructor
        '''
    
    
    def __GetVipUserHead(self,index,count):
        
        content_list = [0 for i in range(0)]
        
        url = "http://www.5show.com/webservice.asmx/GetVipAlbumList?pageIndex="+str(index)+"&pageSize="+str(count)
        host ="www.5show.com"
        print url
        http = MIGHttpMethodGet(url,host)
        http.HttpMethodGet()
        #print http.HttpGetContent()
        root = ElementTree.fromstring(http.HttpGetContent())
        lst_node = root.getiterator("userheadpic")
        for node in lst_node:
            content_list.append(node.text)
        
        return content_list
    
    def __GetAlbumUserHead(self,index,count):
        
        content_list = [0 for i in range(0)]
        
        url = "http://www.5show.com/webservice.asmx/GetAlbumList?pageIndex="+str(index)+"&pageSize="+str(count)
        host ="www.5show.com"
        print url
        http = MIGHttpMethodGet(url,host)
        http.HttpMethodGet()
        #print http.HttpGetContent()
        root = ElementTree.fromstring(http.HttpGetContent())
        lst_node = root.getiterator("userheadpic")
        for node in lst_node:
            content_list.append(node.text)
        
        return content_list
       
    def __GetRobotId(self,index,count):
        content_list = [0 for i in range(0)]
        content = MigHttpInterFace.GetRobotInfo(index, count)
        for element in content:
            content_list.append(element["id"])
        return content_list
         
        
    #更新头像
    def UpdateUserHeadUrl(self):
        #index = 0
        count = 100
        i = 0
        j = 0
        vip_len = 0
        while (j<20000):
            index = j
            content_json_list = [0 for i in range(0)]
            content_list_id = self.__GetRobotId(count,index)
            content_list_url = self.__GetVipUserHead(index+1, count)
            if(len(content_list_url)==0):
                content_list_url = self.__GetAlbumUserHead(index+1-vip_len, count)
            else:
                vip_len = len(content_list_url)
            print content_list_id
            print content_list_url
            print "================"
            if(len(content_list_id)==0 or len(content_list_url)==0):
                break
            
            if len(content_list_id) < len(content_list_url):
                now_len = len(content_list_id) 
            else:
                now_len = len(content_list_url)
            print now_len
            while (i < now_len):
                info = {}
                info["id"] = content_list_id[i]
                info["url"] = content_list_url[i]
                print info
                content_json_list.append(info)
                i = i+1
                
            MigHttpInterFace.UpdateRobotHead(str(json.dumps(content_json_list)))
            j = j + count
            i= 0
            
        
        
        
        