import os
import socket

import math
import struct
import threading
import uuid
import thread
import hashlib
class ObserverInterface(object):
    def __init__(self):
        pass
    def update(self):

        pass


class SubjectInterface(object):
    def __init__(self):
        self.observers = set()
    def addObserver(self, ob):
        self.observers.add(ob)
    def delObserver(self, ob):
        self.observers.remove(ob)
    def notifyObservers(self):
        for ob in self.observers:
            ob.update()


class Observer01(ObserverInterface):
    def __init__(self, sendsize):
        self.sendsize = sendsize
    def update(self):
        try:
            file_object.seek(blocksize*(i-1))
            lock.release()
            num = 0
            sumstr = ''
            while True:
                chunk = file_object.read(sendsize)
                if not chunk:
                    break
                sock.send(chunk)
                sumstr += chunk
                num += len(chunk)
                if num == blocksize:
                    break

        finally:
            # sock.recv(20)
            myhash = hashlib.md5()
            myhash.update(sumstr)
            print myhash.hexdigest()
            print 'ssss'

class Subject01(SubjectInterface):
    def __init__(self):
        SubjectInterface.__init__(self)


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect(('127.0.0.1',9999))
    filename = 'ubuntu-15.04-desktop-amd64.iso'
    randomname = str(uuid.uuid4())+filename
    wholepath = r'/home/hyt/huanrong/'+filename
    file_object = open(wholepath, 'rb')
    sock.send(randomname)
    sock.recv(10)
    filesize = os.path.getsize(wholepath)
    blocksize = 1024*1024*60
    sendsize = 10240
    ob01 = Observer01(sendsize)
    observers = set()
    sb01 = Subject01()
    sb01.addObserver(ob01)
    sendtimes = int(math.ceil(float(filesize)/float(blocksize)))
    sock.send(str(sendtimes))
    sock.recv(10)
    sock.send(str(filesize))
    sock.recv(10)
    sock.send(str(blocksize))
    print sendtimes
    lock = thread.allocate_lock()
    for i in range(1, sendtimes+1, 1):
        lock.acquire_lock()
        sb01.notifyObservers()
