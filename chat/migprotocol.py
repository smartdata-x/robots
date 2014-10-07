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
    
    def packstream(self):
        self.set_packet_length(self.packet_head_length())
        self.set_data_length(0)
        self.headstream()
        return (self.head)
    
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
        
    def packstream(self):
        self.bodystream()
        self.set_packet_length(self.packet_head_length() + len(self.body))
        self.set_data_length(len(self.body))
        self.headstream()
        return (self.head + self.body)
        

        
'''
struct UserLoginSucess:public PacketHead
{
    int64 platform_id;
    int64 user_id;
    int64 nick_number;
    char token[32];
    char nickname[48];
    char head_url[64];
};
'''
   
class LoginSucess(PacketHead):
    def __init__(self):
        PacketHead.__init__(self)
        self.platform_id = 0
        self.user_id = 0
        self.nicknumber = 0
        self.token = ""
        self.nickname = ""
        self.head_url = ""
        
    def set_platform_id(self,platform_id):
        self.platform_id = platform_id
    
    def get_platform_id(self):
        return self.platform_id
    
    def set_user_id(self,user_id):
        self.user_id = user_id
    
    def get_user_id(self):
        return self.user_id
    
    def set_nicknumber(self,nicknumber):
        self.nicknumber = nicknumber
        
    def get_nicknumber(self):
        return self.nicknumber
    
    def set_token(self,token):
        self.token = token
        
    def get_token(self):
        return self.token
    
    def set_nickname(self,nickname):
        self.nickname = nickname
    
    def get_nickname(self):
        return self.nickname
    
    def set_head_url(self,head_url):
        self.head_url = head_url
    
    def get_head_url(self):
        return self.head_url
    
    def unpackstream(self,data):
        self.unpackhead(data)
        self.platform_id,self.user_id,self.nicknumber,self.token,self.nickname,self.head_url=  struct.unpack_from('=qqq32s48s64s',data,31)
        
'''
struct ReqOppstionInfo : public PacketHead{
    int64 platform_id;
    int64 user_id;
    int64 oppostion_id;
    int16 type;
    char token[TOKEN_LEN];
};
'''
    
class ReqOpptionInfo(PacketHead):
    def __init__(self):
        PacketHead.__init__(self)
        self.platform_id = 0
        self.user_id = 0
        self.oppostion_id = 0
        self.opptype = 0
        self.token = ""
    
    def set_platform_id(self,platform_id):
        self.platform_id = platform_id
    
    def set_user_id(self,user_id):
        self.user_id = user_id
    
    def set_oppostion_id(self,oppostion_id):
        self.oppostion_id = oppostion_id
    
    def set_type(self,opptype):
        self.opptype = opptype
    
    def set_token(self,token):
        self.token = token
    
    def bodystream(self):
        self.body = struct.pack('qqqh32s',self.platform_id,self.user_id,self.oppostion_id,
                    self.opptype,self.token)
        
    def packstream(self):
        self.bodystream()
        self.set_packet_length(self.packet_head_length() + len(self.body))
        self.set_data_length(len(self.body))
        self.headstream()
        return (self.head + self.body)
    
    
'''
#define OPPSITIONINFO_SIZE (sizeof(int64) * 2 + NICKNAME_LEN + HEAD_URL_LEN)
struct Oppinfo
{
    int64 user_id;
    int64 user_nicknumber;
    char nickname[NICKNAME_LEN];
    char user_head[HEAD_URL_LEN];

};

//GET_OPPOSITION_INFO = 1021

struct OppositionInfo:public PacketHead{
    int64 platform_id;
    int64 oppo_id;
    int64 oppo_nick_number;
    int64 session;
    int16 oppo_type;
    char  oppo_nickname[NICKNAME_LEN];
    char  oppo_user_head[HEAD_URL_LEN];
    std::list<struct Oppinfo*> opponfo_list;
};
'''
   
class OppositionInfo(PacketHead):
    
    def __init__(self):
        PacketHead.__init__(self)
        self.platform_id = 0
        self.oppo_id = 0
        self.oppo_nick_number = 0
        self.session = 0
        self.oppo_type = 0
        self.oppo_nickname = ""
        self.oppo_user_head = ""
    
    def set_platform_id(self,platform_id):
        self.platform_id = platform_id
    
    def get_platform_id(self):
        return self.platform_id
    
    def set_oppo_id(self,oppo_id):
        self.oppo_id = oppo_id
    
    def get_oppo_id(self):
        return self.oppo_id
    
    def set_oppo_nick_number(self,nicknumber):
        self.oppo_nick_number = nicknumber
    
    def get_oppo_nick_number(self):
        return self.oppo_nick_number
    
    def set_session(self,session):
        self.session = session
    
    def get_session(self):
        return self.session
    
    def set_oppo_type(self,oppo_type):
        self.oppo_type = oppo_type
    
    def get_oppo_type(self):
        return self.oppo_type
    
    def set_oppo_nickname(self,nickname):
        self.oppo_nickname = nickname
    
    def get_oppo_nickname(self):
        return self.oppo_nickname
    
    def set_oppo_user_head(self,head):
        self.oppo_user_head = head
    
    def get_oppo_user_head(self):
        return self.oppo_user_head
    
    def unpackstream(self,data):
        self.unpackhead(data)
        #print  struct.unpack_from('=qqqqh48s64s',data,31)
        self.platform_id,self.oppo_id,self.oppo_nick_number,self.session,self.oppo_type,self.oppo_nickname,self.oppo_user_head =  struct.unpack_from('=qqqqh48s64s',data,31)
        
        

'''
#define MULTISOUNDSEND_SIZE (sizeof(int64) * 4 + sizeof(int16) + TOKEN_LEN + vMultiSoundSend->sound_path.length())
struct MultiSoundSend:public PacketHead{
    int64 platform_id;
    int64 multi_id;// 由客户端产生，同一个类型进入相同的会话
    int16 multi_type;
    int64 send_user_id;
    int64 session;
    char token[TOKEN_LEN];
    std::string sound_path; //文件名: 讨论组id/发送者id/声音文件名(讨论组，发送者，当前时间拼装)
};

'''

class MutilSoundSend(PacketHead):
    
    def __init__(self):
        PacketHead.__init__(self)
        self.platform_id = 0
        self.multi_id = 0;
        self.multi_type = 0
        self.send_user_id = 0
        self.session = 0
        self.token = ""
        self.path = ""
    
    def set_platform_id(self,platform_id):
        self.platform_id = platform_id
    
    def get_platform_id(self):
        return self.platform_id
    
    def set_multi_id(self,multi_id):
        self.multi_id = multi_id
    
    def get_multi_id(self):
        return self.multi_id
    
    def set_multi_type(self,multi_type):
        self.msg_type = multi_type
    
    def get_multi_type(self):
        return self.multi_type
    
    def set_send_user_id(self,user_id):
        self.send_user_id = user_id
    
    def get_send_user_id(self):
        return self.send_user_id
    
    def set_session(self,session):
        self.session = session
    
    def get_session(self):
        return self.session
    
    def set_token(self,token):
        self.token = token
        
    def get_token(self):
        return self.token
    
    def set_sound_path(self,sound_path):
        self.path = sound_path
        
    def get_sound_path(self):
        return self.path
    
    def bodystream(self):
        str_formart = '=qqhqq32s%ds' %(len(self.path))
        self.body = struct.pack(str_formart,self.platform_id,self.multi_id,self.msg_type,
                   self.send_user_id,self.session,self.token,self.path)
                   
        
    def packstream(self):
        self.bodystream()
        self.set_packet_length(self.packet_head_length() + len(self.body))
        self.set_data_length(len(self.body))
        self.headstream()
        return (self.head + self.body)
    
'''
    struct ChatFailed:public PacketHead{
        int64 platform_id;
        std::stringcontent
    };
'''   
class ChatFailed(PacketHead):
    def __init__(self):
        PacketHead.__init__(self)
        self.platform_id = 0
        self.error = ""
        
    def set_platform_id(self,platform_id):
        self.platform_id = platform_id
    
    def get_platform_id(self):
        return self.platform_id
    
    def set_error(self,error):
        self.error = error
    
    def get_error(self):
        return self.error
    
    def unpackstream(self,data):
        self.packet_length,self.operate_code,self.data_length = self.unpackhead(data)
        self.platform_id= struct.unpack_from('=q',data,31)
        error_len = self.data_length - 8
        str_format = '%ds' % (error_len)
        self.error = struct.unpack_from(str_format,data,31+(self.data_length - error_len))
'''
struct TextChatPrivateSend:public PacketHead{
    int64 platform_id;
    int64 send_user_id;
    int64 recv_user_id;
    int64 session;
    char token[TOKEN_LEN];
    std::string content;
};
'''     
class TextChatPrivateSend(PacketHead):
    def __init__(self):
        PacketHead.__init__(self)
        self.platform_id = 0
        self.send_user_id = 0
        self.recv_user_id = 0
        self.session = 0
        self.token = ""
        self.content = ""
        
    def set_platform_id(self,platform_id):
        self.platform_id = platform_id
    
    def get_platform_id(self):
        return self.platform_id
    
    def set_send_user_id(self,send_user_id):
        self.send_user_id = send_user_id
    
    def get_send_user_id(self):
        return self.send_user_id
    
    def set_recv_user_id(self,recv_user_id):
        self.recv_user_id = recv_user_id
    
    def get_recv_user_id(self):
        self.recv_user_id
        
    def set_token(self,token):
        self.token = token
    
    def get_token(self):
        return self.token
    
    def set_session(self,session):
        self.session = session
    
    def get_session(self):
        return self.session
    
    def set_content(self,content):
        self.content = content
    
    def get_content(self):
        return self.content
    
    def bodystream(self):
       
        str_formart = '=qqqq32s%ds' %(len(str(self.content)))
        self.body = struct.pack(str_formart,self.platform_id,self.send_user_id,
                   self.recv_user_id,self.session,self.token,str(self.content))
                   
        
    def packstream(self):
        self.bodystream()
        self.set_packet_length(self.packet_head_length() + len(self.body))
        self.set_data_length(len(self.body))
        self.headstream()
        return (self.head + self.body)
    
      
'''
struct TextChatPrivateRecv:public PacketHead{
    int64 platform_id;
    int64 send_user_id;
    int64 recv_user_id;
    std::string content;
};
'''
   
class TextChatPrivateRecv(PacketHead):
    def __init__(self):
        PacketHead.__init__(self)
        self.platform_id = 0
        self.send_user_id = 0
        self.recv_user_id = 0
        self.content = ""
        
    def set_platform_id(self,platform_id):
        self.platform_id = platform_id
    
    def get_platform_id(self):
        return self.platform_id
    
    def set_send_user_id(self,send_user_id):
        self.send_user_id = send_user_id
    
    def get_send_user_id(self):
        return self.send_user_id
    
    def set_recv_user_id(self,recv_user_id):
        self.recv_user_id = recv_user_id
    
    def get_recv_user_id(self):
        self.recv_user_id
    
    def set_content(self,content):
        self.content = content
    
    def get_content(self):
        return self.content
    
    def unpackstream(self,data):
        self.packet_length,self.operate_code,self.data_length = self.unpackhead(data)
        content_len = self.data_length -  24
        str_format = '=qqq%ds' % (content_len)
        self.platform_id,self.send_user_id,self.recv_user_id,self.content= struct.unpack_from(str_format,data,31)
    
    

        