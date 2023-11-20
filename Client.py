import threading
import socket
from tkinter import *

root = Tk()
root.title("Chat Room")

root.grid()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 12345
s.connect((host,port))
#print("Connected")

def PLACEHOLDER():
    pass

def SEND():
    while True:
        data = input()
        s.sendall(data.encode())

def RECIEVE():
    while True:
        data = s.recv(1024)
        print("                  ",data.decode())

#t1 = threading.Thread(target = SEND)
#t2 = threading.Thread(target = RECIEVE)

Label1 = Label(root, text = "Enter a username", font = ("Arial",12,"bold"))
Label1.grid(row = 0, column = 2)

entry1 = Entry(root)
entry1.grid(row = 1, column = 2)

buttonEnter = Button(root, text = "Enter", command = lambda: PLACEHOLDER())
buttonEnter.grid(row = 2, column = 2)

#t2.start()
#t1.start()

root.mainloop()