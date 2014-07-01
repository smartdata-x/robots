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
    
    def get_uid(self):
        return self.uid
    
    def get_songid(self):
        return self.songid
    
    def get_latitude(self):
        return self.latitude
    
    def get_longitude(self):
        return self.longitude
    
    def get_nickname(self):
        return self.nickname
        
    @classmethod 
    def packet_len(cls):
        return 8 * 2 + 4 * 2 + 48
     
class NoticeRobotLogin(PacketHead):
    
    def __init__(self):
        PacketHead.__init__(self)
        self.uid = 0
        self.robotlist =[ 0 for i in range(0)]
        
    def getrobotlist(self):
        return self.robotlist
    
    def getuid(self):
        return self.uid
    
    def unpackstream(self,data):
        self.packet_length,self.operate_code,self.data_length = self.unpackhead(data)
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

'''
struct RobotLogin:public PacketHead{
    int64 platform_id;
    int64 uid;
    int64 robot_id;
};
'''    
class RobotLogin(PacketHead):
    def __init__(self):
        PacketHead.__init__(self)
    
    def set_platform_id(self,platform_id):
        self.platform_id = platform_id
    
    def set_uid(self,uid):
        self.uid = uid
    
    def set_robot_id(self,robot_id):
        self.robot_id = robot_id
    
    def bodystream(self):
        self.body = struct.pack('=qqq',self.platform_id,self.uid,self.robot_id)
        
    def packstream(self):
        self.bodystream()
        self.set_packet_length(self.packet_head_length() + len(self.body))
        self.set_data_length(len(self.body))
        self.headstream()
        return (self.head + self.body)
        
        
'''
//NOTICE_USER_ROBOT_HANDSEL_SONG
#define NOTICEUSERROBOTHANDSELSONG_SIZE  (sizeof(int64) * 3)
struct NoticeUserRobotHandselSong:public PacketHead{
    int64 platform_id;
    int64 uid;
    int64 robot_id;
};
'''
class NoticeRobotHandselSong(PacketHead):
    def __init__(self):
        PacketHead.__init__(self)
        self.platform_id = 0
        self.uid = 0
        self.robot_id = 0
        self.songid = 0
    
    def get_platform_id(self):
        return self.platform_id
    
    def get_uid(self):
        return self.uid
    
    def get_robot_id(self):
        return self.robot_id
    
    def get_song_id(self):
        return self.songid
    
    def unpackstream(self,data):
        self.platform_id,self.uid,self.robot_id,self.songid = struct.unpack_from('=qqqq',data,31)

'''
//NOTICE_USER_ROBOT_LISTEN_SONG
#define NOTICEUSERROBOTLISTENSONG_SIZE (sizeof(int64) * 2 + sizeof(int32) + MODE_LEN + NAME_LEN + SINGER_LEN)
struct NoticeUserListenSong:public PacketHead{
    int64 platform_id;
    int64 songid;
    int32 typid;
    char mode[MODE_LEN];
    char name[NAME_LEN];
    char singer[SINGER_LEN];
};
'''
class NoticeUserRobotListenSong(PacketHead):
    def __init__(self):
        PacketHead.__init__(self)
        self.platform_id = 0
        self.songid = 0
        self.typeid = 0
    
    def get_platform_id(self):
        return self.platform_id
    
    def get_song_id(self):
        return self.songid
    
    def get_type_id(self):
        return self.typeid
    
    def get_mode(self):
        return self.mode
    
    def get_name(self):
        return self.name
    
    def get_singer(self):
        return self.singer 
    
    def unpackstream(self,data):
        self.platform_id,self.songid,self.typeid,self.mode,self.name,self.singer= struct.unpack_from('=qqi32s128s128s',data,31)

        
'''
#define NOTICEASSISTANTLOGIN_SIZE (sizeof(int64) * 2 + NICKNAME_LEN)
struct NoticeAssistantLogin:public PacketHead{
    int64 platform_id;
    int64 assistant_id;
    char nickname[NICKNAME_LEN];
};
'''
class NoticeAssistantLogin(PacketHead):
   
    def __init__(self):
        PacketHead.__init__(self)
        self.platform_id = 0
        self.assistant_id = 0
        self.nickname = ""
    
    def get_platformid(self):
        return self.platform_id
    
    def get_assistantid(self):
        return self.assistant_id
    
    def get_nickname(self):
        return self.nickname
    
    def unpackstream(self,data):
        self.platform_id,self.assistant_id,self.nickname = struct.unpack_from('=qq48s',data,31)
        
        
        
'''
//ASSISTANT_LOGIN_SUCCESS
#define ASSISTANTLOGINSUCCESS_SIZE (sizeof(int64) * 2)
struct AssistantLoginSuccess:public PacketHead{
    int64 platform_id;
    int64 assistant_id;
};
'''
        
class AssistantLogin(PacketHead):
    def __init__(self):
        PacketHead.__init__(self)
        self.platform_id = 0
        self.uid = 0
    
    def set_platform_id(self,platform_id):
        self.platform_id = platform_id
        
    def set_uid(self,uid):
        self.uid = uid
    
    def bodystream(self):
        self.body = struct.pack('=qq',self.platform_id,self.uid,)
        
    def packstream(self):
        self.bodystream()
        self.set_packet_length(self.packet_head_length() + len(self.body))
        self.set_data_length(len(self.body))
        self.headstream()
        return (self.head + self.body)
    
class ElementHanlseSong():
    def __init__(self):
        self.uid = 0
        self.songid = 0
        self.message = ""
    
    def set_uid(self,uid):
        self.uid = uid
    
    def set_songid(self,songid):
        self.songid = songid
        
    def set_message(self,message):
        self.message = message
    
    def get_uid(self):
        return self.uid 
    
    def get_songid(self):
        return self.songid
    
    def get_message(self):
        return self.message
    
    @classmethod
    def packet_len(cls):
        return 8 * 2 + 512
    
class NoticeAssistantHandlseSong(PacketHead):
    
    def __init__(self):
        PacketHead.__init__(self)
        self.platform_id = 0
        self.assistant_id = 0
        self.handlselist = [0 for i in range(0)]
    
    def gethandlselist(self):
        return self.handlselist
    
    def get_platform_id(self):
        return self.platform_id
    
    def get_assistant_id(self):
        return self.assistant_id
    
    def unpackstream(self,data):
        self.packet_length,self.operate_code,self.data_length = self.unpackhead(data)
        i = 0
        n = (self.data_length - 8) / ElementHanlseSong.packet_len()
        self.platform_id,self.assistant_id,tempuid= struct.unpack_from('=qqq',data,31)
        miglog.log().debug(self.platform_id)
        miglog.log().debug(self.assistant_id)
        while(n>0):
            element = ElementHanlseSong()
            uid,songid,message = struct.unpack_from('=qq512s',data,31+8*2+i*ElementHanlseSong.packet_len())
            n = n -1
            i = i+1
            #print uid,songid,message
            miglog.log().debug(uid)
            miglog.log().debug(songid)
            miglog.log().debug(message)
            
            element.set_uid(uid)
            element.set_songid(songid)
            element.set_message(message)
            self.handlselist.append(element)
    