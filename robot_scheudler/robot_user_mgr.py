#!/usr/bin/python2.6  
# -*- coding: utf-8 -*-  
#encoding=utf-8

'''
Created on 2014年6月17日

@author: kerry
'''
from robot_scheudler import robot_protocol
from base.miglog import miglog
from multiprocessing import Process,Pool,Pipe
from robot_scheudler.robot_netservice import MIGRobotInitialScheduler
from robot_scheudler.assistant_netservice import MIGAssistantInitialScheduler
from chat.netservice import MIGSchedulerClient as MIGChatInitialScheduler
#from robot_scheudler.chat_netservice import MIGChatInitialScheduler

def RobotChatLogin(data):
    miglog.log().debug(data["platform"])
    miglog.log().debug(data["uid"])
    robot_chat_client = MIGChatInitialScheduler()
    robot_chat_client.set_platform_id(data["platform"])
    robot_chat_client.set_uid(data["robotid"])
    robot_chat_client.set_oppid(data["uid"])
    robot_chat_client.set_token("token")
    robot_chat_client.set_oppo_type(1)
    #robot_chat_client.Connection("42.121.14.108", 17000) 
    robot_chat_client.Connection("112.124.49.59", 17000)
    robot_chat_client.start_run()

def RobotLogin(data):
    robot = data["robot"]
    miglog.log().debug(robot.get_latitude())
    miglog.log().debug(robot.get_longitude())
    miglog.log().debug(robot.get_uid())
    robot_client = MIGRobotInitialScheduler()
    robot_client.set_platform_id(data["platform"])
    robot_client.set_robot_id(robot.get_uid())
    robot_client.set_uid(data["uid"])
    #robot_client.Connection("42.121.14.108", 19008)
    robot_client.Connection("112.124.49.59", 19008)
    robot_client.start_run()

def AssistantLogin(data):
    miglog.log().debug(data["platform"])
    miglog.log().debug(data["uid"])
    assistant_client = MIGAssistantInitialScheduler()
    assistant_client.set_platform_id(data["platform"])
    assistant_client.set_uid(data["uid"])
    assistant_client.set_nickname(data["nickname"])
    #assistant_client.Connection("42.121.14.108", 19008)
    assistant_client.Connection("112.124.49.59", 19008)
    assistant_client.start_run()

    
    
    
    
class RobotUserMgr(object):
    '''
    classdocs
    '''


    def __init__(self,host,port):
        '''
        Constructor
        '''
        self.platform_id = 0
        self.host = host
        self.port = port
        
    def SchdulerLogin(self,platform_id,machine_id):
        self.platform_id = platform_id
        login = robot_protocol.LoginPacket()
        login.make_head(2000,1, 0, 0)
        login.set_platform_id(platform_id)
        login.set_machine_id(machine_id)
        return login.packstream()
    
    
    def NoticeRobotChat(self,data):
        robot_chat_login = robot_protocol.NoticeRobotChatLogin()
        robot_chat_login.unpackstream(data)
        pool = Pool(processes=1)
        element = {}
        element["platform"] = robot_chat_login.get_platform_id()
        element["uid"] = robot_chat_login.get_uid()
        element["robotid"] = robot_chat_login.get_robotid()
        result = pool.apply_async(RobotChatLogin, [element])
        pool.close()
        
        

        
    def NoticeAssistantInfo(self,data):
        assistant_login = robot_protocol.NoticeAssistantLogin()
        assistant_login.unpackstream(data)
        pool = Pool(processes=1)
        element = {}
        element["platform"] = assistant_login.get_platformid()
        element["uid"] = assistant_login.get_assistantid()
        element["nickname"] = assistant_login.get_nickname()
        result = pool.apply_async(AssistantLogin, [element])
        pool.close()
        #pool.join()
    
    def NoticeRobotInfo(self,data):
        robotlist =[ 0 for i in range(0)]
        robot_login = robot_protocol.NoticeRobotLogin()
        robot_login.unpackstream(data)
        robot_list = robot_login.getrobotlist()
        miglog.log().debug(len(robot_list))
        #独立用户开辟一个进程 用户模拟用户操作  传送机器人信息和用户id
        if(len(robot_list)>0):
            pool = Pool(processes=len(robot_list))
            for robot in robot_list:
                element = {}
                element["platform"] = self.platform_id
                element["host"] = self.host
                element["port"] = self.port
                element["uid"] =  robot_login.getuid()
                element["robot"] = robot
                result = pool.apply_async(RobotLogin, [element])
            pool.close()
            #pool.join() 只用创建无需等待进程完成
        