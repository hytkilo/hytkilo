import socket
import struct
import os
import threading
from time import sleep
import hashlib


def serverupload(newsock):
    print 'hello'
    sum = 0
    myfilename = newsock.recv(100)
    newsock.send('ok')
    recvtime = int(newsock.recv(4))
    newsock.send('ok')
    filesize = long(newsock.recv(20))
    newsock.send('ok')
    blocksize = newsock.recv(10)
    print myfilename, recvtime
    for i in range(1, recvtime + 1, 1):
        if i == recvtime:
            blocksize = filesize % int(blocksize)
        new_path_filename = r'/home/hyt/huanrong/b/' + myfilename + '.part' + str(i)
        print new_path_filename
        file_object = open(new_path_filename, 'w+')
        num = 0
        while num < int(blocksize):
            recvdata = newsock.recv(10240)
            file_object.write(recvdata)
            num += len(recvdata)
            file_object.flush()
        # socket.send('finish')
        file_object.close()
        md5obj = hashlib.md5()
        maxbuf = 8192
        f = open(new_path_filename, 'rb')
        while True:
            buf = f.read(maxbuf)
            if not buf:
                break
            md5obj.update(buf)
        f.close()
        hashcode = md5obj.hexdigest()
        print hashcode
        print 'end'
        sum += os.path.getsize(new_path_filename)
    print sum


if __name__ == '__main__':
    host = '127.0.0.1'
    port = 9999
    socket =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket.bind((host,port))
    socket.listen(5)
    while True:
        sock, address = socket.accept()
        print "accept another connection"
        thread = threading.Thread(target=serverupload, args=(sock,))
        thread.setDaemon(True)
        thread.start()




