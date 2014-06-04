#!/usr/bin/python2.6  
# -*- coding: utf-8 -*-  
#encoding=utf-8

'''
Created on 2014年5月28日

@author: kerry
'''

import struct


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
struct UserLogin:public PacketHead{
    int64 platform_id;
    int64 user_id;
    int8  net_type;
    int8  user_type;
    int8  device;
    char  token[32];
};

'''  
class LoginPacket(PacketHead):
    def __init__(self):
        PacketHead.__init__(self) 
        
    def set_platform_id(self,platform_id):
        self.platform_id = platform_id
    
    def set_user_id(self,user_id):
        self.user_id = user_id
    
    def set_net_type(self,net_type):
        self.net_type = net_type
    
    def set_user_type(self,user_type):
        self.user_type = user_type
        
    def set_device(self,device):
        self.device = device
    
    def set_token(self,token):
        self.token = token
    

        
    def bodystream(self):
        self.body = struct.pack('qqbbb32s',self.platform_id,self.user_id,self.net_type,
                    self.user_type,self.device,self.token)
        print len(self.body)
        
    def packstream(self):
        self.bodystream()
        self.set_packet_length(self.packet_head_length() + len(self.body))
        self.set_data_length(len(self.body))
        self.headstream()
        print len(self.head + self.body)
        return (self.head + self.body)
        

        
        
        