#!/usr/bin/python2.6  
# -*- coding: utf-8 -*-  
#encoding=utf-8
'''
Created on 2014年7月2日

@author: kerry
'''
from base.miglog import miglog
import sys
import struct

class NetData(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.structFormat = "=i"
        self.prefixLength = struct.calcsize(self.structFormat)
        self._unprocessed = ""
        self.PACKET_MAX_LENGTH = 99999
        
    def net_wok(self,data):
                #取前4个字节
        alldata = self._unprocessed + data
        currentOffset = 0
        fmt = self.structFormat
        self._unprocessed = alldata
        miglog.log().debug("alldata %d unprocessed %d data %d",len(alldata),len(self._unprocessed),len(data))
        while len(alldata) >=(currentOffset + self.prefixLength):
            messageStart = currentOffset + self.prefixLength
            length, = struct.unpack(fmt,alldata[currentOffset:messageStart])
            if length > self.PACKET_MAX_LENGTH:
                self._unprocessed = alldata
                self.lenthLimitExceeded(length)
                return
            messageEnd = currentOffset + length
            miglog.log().debug("length %d len(dlldata) %d messageEnd(%d)",length,len(alldata),messageEnd)
            if len(alldata) < messageEnd:
                packet = ""
                result = 0
                miglog.log().debug("=====================")
                break
            packet = alldata[currentOffset:messageEnd]
            currentOffset = messageEnd
            result = 1
        
        self._unprocessed = alldata[currentOffset:]
        return packet,result