import socket
import threading
import time

tLock = threading.Lock()
shutdown = False

def receving(name, sock):
    while not shutdown:
            try:
                tLock.acquire()
                while True:
                        data,addr = sock.recvfrom(1024)
                        print(str(data))
            except:
                    pass
            finally:
                    tLock.release()

#host = '192.168.26.86'
host = '127.0.0.1'
port = 0 #pick any free port currently on the computer
server = (host, 5000)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host,port))
s.setblocking(0)

#receiving thread
rT = threading.Thread(target=receving, args=("RecvThread", s))
rT.start()

alias = raw_input("Name: ")

#PLAYER ENTERS DATA
message = raw_input(alias + "First msg ->")

while message != 'q':
        tLock.acquire()
        message = raw_input(alias + "What is your answer ?  ->")
        tLock.release()


        if message != '':
            s.sendto(alias + ": " + message, server)

        time.sleep(0.2)

shutdown = True
rT.join()
s.close()