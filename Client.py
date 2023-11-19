import threading
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 12345
s.connect((host,port))
#print("Connected")

def SEND():
    while True:
        data = input()
        s.sendall(data.encode())

def RECIEVE():
    while True:
        data = s.recv(1024)
        print("                  ",data.decode())

t1 = threading.Thread(target = SEND)
t2 = threading.Thread(target = RECIEVE)


t2.start()
t1.start()