import itertools
import hashlib
import os
import struct
import SocketServer
import logging
import base64
import socket

import sys, Queue, threading, hashlib, os

NumOfThreads = 10  # Number of threads; max ~ 25k
queue = Queue.Queue()

s = socket.socket()
s.connect(("five-blocks.2016.volgactf.ru", 8888))
data = s.recv(1024)
print data
challenge = data.split("==")[3].strip()

charset = ''
for i in range(256):
    charset += chr(i)




class checkHash(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            self.clear = self.queue.get()
            h = hashlib.sha1(self.clear).digest()
            print h
            if h[-3:] == '\xff\xff\xff':
                print ("challenge solved %s for %s " % (self.clear, challenge))
                os._exit(0)
            self.queue.task_done()


for i in range(NumOfThreads):
    t = checkHash(queue)
    t.setDaemon(True)
    t.start()

for word in itertools.product(charset, repeat=5):
    queue.put(challenge + ''.join(word))

queue.join()