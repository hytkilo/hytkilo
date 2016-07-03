import os
import socket

import math

if __name__ == '__main__':
    socket =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket.connect(('127.0.0.1',9999))
    filename = 'ubuntu-15.04-desktop-amd64.iso'
    wholepath = r'/home/hyt/huanrong/'+filename
    file_object = open(wholepath, 'rb')
    socket.send(filename)
    filesize = os.path.getsize(wholepath)
    sendsize = 10240
    sendtimes =long(math.ceil(float(filesize)/float(sendsize)))
    socket.send(str(sendtimes))
    print sendtimes
    try:
        while True:
            chunk = file_object.read(sendsize)
            if not chunk:
                break
            socket.send(chunk)
    finally:
        file_object.close()
