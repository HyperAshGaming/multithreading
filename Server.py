import threading
import socket
from tkinter import *

root = Tk()
root.title("Chat Room")

root.grid()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ''
port = 12345
s.bind((host,port))
s.listen(5)
conn, addr = s.accept()

def PLACEHOLDER():
    pass

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

#Enter Username

#Line

#Enter Button

Label1 = Label(root, text = "Enter a username", font = ("Arial",12,"bold"))
Label1.grid(row = 0, column = 2)

entry1 = Entry(root)
entry1.grid(row = 1, column = 2)

buttonEnter = Button(root, text = "Enter", command = lambda: PLACEHOLDER())
buttonEnter.grid(row = 2, column = 2)



#t1.start()
#t2.start()

root.mainloop()