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


def RobotLogin(data):
    robot = data["robot"]
    miglog.log().debug(robot.get_latitude())
    miglog.log().debug(robot.get_longitude())
    miglog.log().debug(robot.get_uid())
    robot_client = MIGRobotInitialScheduler()
    robot_client.set_platform_id(data["platform"])
    robot_client.set_robot_id(robot.get_uid())
    robot_client.set_uid(data["uid"])
    robot_client.Connection("112.124.49.59", 19008)
    robot_client.start_run()
    
    
    
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
        