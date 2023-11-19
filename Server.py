import threading
import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ''
port = 12345
s.bind((host,port))
s.listen(5)
#print('Socket is listening')
conn, addr = s.accept()
#print('Got a connection from', addr)

def SEND():
    while True:
        data = input()
        conn.sendall(data.encode())

def RECIEVE():
    while True:
        data = conn.recv(1024)
        print("                  ",data.decode())

t1 = threading.Thread(target = SEND)
t2 = threading.Thread(target = RECIEVE)

t1.start()
t2.start()