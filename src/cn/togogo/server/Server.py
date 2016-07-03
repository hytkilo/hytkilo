import socket
if __name__ == '__main__':
    host = '127.0.0.1'
    port = 9999
    socket =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket.bind((host,port))
    socket.listen(5)
    while True:
        newsock, address = socket.accept()
        print "accept another connection"
        myfilename = newsock.recv(40)
        recvtime = long(newsock.recv(20))

        new_path_filename = r'/home/hyt/huanrong/b/'+myfilename
        file_object = open(new_path_filename, 'w')
        for i in range(1,recvtime+1,1):
            recvdata = newsock.recv(10240)
            file_object.write(recvdata)
            file_object.flush()
        file_object.close()
        print 'end'





