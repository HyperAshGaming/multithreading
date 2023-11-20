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

black = (0,0,0)

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

#Defining all frames
ChatRoomFrame = Frame(root)
EnterRoomFrame = Frame(root)
CreateRoomFrame = Frame(root)

#Initial Frame Grid
CreateRoomFrame.grid(row = 0, column = 0)

#CreateRoomFrame
ButtonJoin = Button(CreateRoomFrame, text = "Join a room", command = lambda: PLACEHOLDER())
ButtonJoin.grid(row = 0, column = 0)

ButtonCreate = Button(CreateRoomFrame, text = "Create a room", command = lambda: PLACEHOLDER())
ButtonCreate.grid(row = 1, column = 0)



#EnterRoomFrame
LabelUSEnter = Label(EnterRoomFrame, text = "Enter a username", font = ("Arial",12,"bold"))
LabelUSEnter.grid(row = 0, column = 2)

entry1 = Entry(EnterRoomFrame)
entry1.grid(row = 1, column = 2)

buttonEnter = Button(EnterRoomFrame, text = "Enter", command = lambda: PLACEHOLDER())
buttonEnter.grid(row = 2, column = 2)



#t1.start()
#t2.start()

root.mainloop()


#Create window asking to create or enter room

#Enter Window: Username and RoomID

#Create Window: Creates Window

#Create Chat Room