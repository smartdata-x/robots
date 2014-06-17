#!/usr/bin/python2.6  
# -*- coding: utf-8 -*-  
#encoding=utf-8

'''
Created on 2014年6月16日

@author: kerry
'''

import struct
from base.miglog import miglog


'''
struct PacketHead{
   int32 packet_length;
   int32 operate_code;
   int32 data_length;
   int32 current_time;
   int16 msg_type;
   int8  is_zip;
   int64 msg_id;
   int32 reserverd;
};
'''
class PacketHead:
    def __init__(self):
        pass
    
    def set_packet_length(self,packet_length):
        self.packet_length = packet_length
    
    def set_operate_code(self,operate_code):
        self.operate_code = operate_code
        
    def set_data_length(self,data_length):
        self.data_length = data_length
    
    def set_current_time(self,current_time):
        self.current_time = current_time
    
    def set_msg_type(self,msg_type):
        self.msg_type = msg_type
    
    def set_is_zip(self,is_zip):
        self.is_zip = is_zip
    
    def set_msg_id(self,msg_id):
        self.msg_id = msg_id
        
    def set_reserved(self,reserved):
        self.reserved = reserved
    
    def headstream(self):
        self.head  = struct.pack('=iiiihbqi',self.packet_length,self.operate_code,self.data_length,
                            self.current_time,self.msg_type,self.is_zip,self.msg_id,self.reserved)
     
    def packet_head_length(self):
        return 31

    
    def make_head(self,operate_code,msg_type,is_zip,reserved):
        self.set_operate_code(operate_code)
        self.set_current_time(0)
        self.set_msg_type(msg_type)
        self.set_is_zip(is_zip)
        self.set_msg_id(0)
        self.set_reserved(reserved)
    
    def unpackhead(self,packet_stream):
        return  struct.unpack_from('=iii',packet_stream)


'''
struct SchedulerLogin:public PacketHead{
    int64 platform_id;
    std::string machine_id;
};
'''
    
class LoginPacket(PacketHead):
    def __init__(self):
        PacketHead.__init__(self) 
        
    def set_platform_id(self,platform_id):
        self.platform_id = platform_id
    
        
    def set_machine_id(self,machine_id):
        self.machine_id = machine_id
    

        
    def bodystream(self):
        str_formar = '=q%ds' %(len(self.machine_id))
        self.body = struct.pack(str_formar,self.platform_id,self.machine_id)
        
    def packstream(self):
        self.bodystream()
        self.set_packet_length(self.packet_head_length() + len(self.body))
        self.set_data_length(len(self.body))
        self.headstream()
        return (self.head + self.body)
        


'''
#define ROBOTINFO_SIZE (sizeof(int64) * 2 + sizeof(int32) * 2 + NICKNAME_LEN)
struct RobotInfo{
    int64 uid;
    int64  songid;
    double latitude;
    double longitude;
    char nickname[NICKNAME_LEN];
};
//NOTICE_USER_ROBOT_LOGIN
struct NoticeRobotLogin:public PacketHead{
    int64 uid;
    std::list<struct RobotInfo*> robot_list;
};
'''

class ElementRobotInfo():
    def __init__(self):
        self.uid = 0
        self.songid = 0
        self.latitude = 0
        self.longitude = 0
        self.nickname = ""
    
    def set_uid(self,uid):
        self.uid = uid
    
    def set_songid(self,songid):
        self.songid = songid
    
    def set_latitude(self,latitude):
        self.latitude = latitude
    
    def set_longitude(self,longitude):
        self.longitude = longitude
    
    def set_nickname(self,nickname):
        self.nickname = nickname
        
    @classmethod 
    def packet_len(cls):
        return 8 * 2 + 4 * 2 + 48
     
class NoticeRobotLogin(PacketHead):
    
    def __init__(self):
        PacketHead.__init__(self)
        self.uid = 0
        self.robotlist =[ 0 for i in range(0)]
        
    def unpackstream(self,data):
        self.packet_length,self.operate_code,self.data_length = self.unpackhead(data)
        print self.data_length
        i = 0
        n = (self.data_length - 8) / ElementRobotInfo.packet_len()
        self.uid,tmpuid= struct.unpack_from('=qq',data,31)
        while(n>0):
            element = ElementRobotInfo()
            uid,songid,latitude,longitude,nickname = struct.unpack_from('=qqii48s',data,31+8+i*ElementRobotInfo.packet_len())
            n = n -1
            i = i+1
            #print uid,songid,latitude,longitude,nickname
            element.set_uid(uid)
            element.set_songid(songid)
            element.set_latitude(latitude)
            element.set_longitude(longitude)
            element.set_nickname(nickname)
            self.robotlist.append(element)
            
        #self.uid,self.ruid,self.songid = struct.unpack_from('=qqq',data,31)

    

        