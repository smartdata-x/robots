#!/usr/bin/python2.7  
# -*- coding: utf-8 -*-

'''
@author: along
'''

import time 
import threading 
import Queue 
import util
import weiboclient

class weiboThread(threading.Thread): 
    def __init__(self, client, msgqueue, outqueue): 
        threading.Thread.__init__(self)
        self._client = client
        self._queue = msgqueue
        self._outqueue = outqueue 

    def run(self):
        response = {}
        requests = {}
        while True: 
            if self._queue.empty() == False:
                contents = self._queue.get() 
                for key in contents.keys():
                    content = contents[key]
                    request = self._client.requestXiaobing(content)
                    requests[content] = request
                    response[key] = requests
                    self._outqueue.put(response)
                contents.clear()
        print 'Bye byes!'


class callbackThread(threading.Thread): 
    def __init__(self, callback, outqueue): 
        threading.Thread.__init__(self)
        self._callback = callback
        self._outqueue = outqueue 

    def run(self):
        while True: 
            if self._outqueue.empty() == False:
                response = self._outqueue.get() 
                for key in response.keys():
                    contents = response[key]
                    for contentkey in contents.keys():
                        self._callback(key, contents[contentkey])
                    contents.clear()
                response.clear()
        print 'Bye byes!'

def build_worker_pool(queue, outqueue):
    workers = []
    logininfo = util.getWeiboLoginInfo()
    for item in logininfo:
        client = weiboclient.get_client(item[0], item[1], item[2], item[3])
        if client:
            worker = weiboThread(client, queue, outqueue)
            worker.start() 
            workers.append(worker)
    return workers

def build_callback_thread(callback, queue):
    callThread = callbackThread(callback, queue)
    callThread.start()
    return callThread

class weiboService(object):
    def __init__(self, callback):
        self.queue = Queue.Queue()
        self.outQueue = Queue.Queue()
        self.workerThreads = build_worker_pool(self.queue, self.outQueue)
        self.callbackThread = build_callback_thread(callback, self.outQueue)
        self.contens = {}
        
    def requestXiaobing(self, clientid, content):
        contents = {}
        contents[clientid] = content
        self.queue.put(contents)
        
def getWeibo(callback):
    return weiboService(callback)