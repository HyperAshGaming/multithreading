import threading
import socket
import sqlite3
from tkinter import *

connsqlite = sqlite3.connect('Chat.db')
c = connsqlite.cursor()

root = Tk()
root.title("Chat Room SERVER")

root.grid()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ''
port = 12345
s.bind((host,port))
s.listen(5)
conn, addr = s.accept()

def SEND():
    global MessageEntry
    global r
    print(m,r)
    MessageSent = Label(CreateRoomFrame, text = m, font = ("Arial",12,"bold"))
    MessageSent.grid(row = r, column = 1)
    r += 1
    data = m
    conn.sendall(data.encode())

def RECIEVE():
    r += 1
    while True:
        data = conn.recv(1024)
        print("                  ",data.decode())

def PLACEHOLDER():
    print(entryIDenter.get(),entryUSEnter.get())
    c.execute("SELECT * from roomtable1")
    for i in c:
        if i[0] == int(entryIDenter.get()):
            c.execute("SELECT * from roomtable1")
            for j in c:
                if j[2] == entryUSEnter.get():
                    test()
                    break

def test():
    ChatRoomFrame.config(width = 500, height = 500)
    EnterRoomFrame.destroy()
    ChatRoomFrame.grid(row = 50, column = 150)
    ChatRoomFrame.pack()


    #JoinChatRoomText = Label(CreateRoomFrame, text = name+"", font = ("Arial",12,"bold"))

def RoomEnterFrame():
    DecideRoomFrame.destroy()
    EnterRoomFrame.grid(row = 0, column = 0)

def RoomCreateFrame():
    DecideRoomFrame.destroy()
    CreateRoomFrame.grid(row = 0, column = 0)

def xyz():
    t1.start()
    t2.start()

t1 = threading.Thread(target = SEND)
t2 = threading.Thread(target = RECIEVE)

black = (0,0,0)

r = 0

#Defining all frames
ChatRoomFrame = Frame(root, width = 50, height = 150)
EnterRoomFrame = Frame(root)
CreateRoomFrame = Frame(root)
DecideRoomFrame = Frame(root)

MessageFrame = Frame(ChatRoomFrame)
MessageFrame.grid(row = 1, column = 0)


#Initial Frame Grid
DecideRoomFrame.grid(row = 0, column = 0)

#DecideRoomFrame
ButtonJoin = Button(DecideRoomFrame, text = "Join a room", command = lambda: RoomEnterFrame())
ButtonJoin.grid(row = 0, column = 0)

ButtonCreate = Button(DecideRoomFrame, text = "Create a room", command = lambda: RoomCreateFrame())
ButtonCreate.grid(row = 1, column = 0)

#EnterRoomFrame
LabelIDEnter = Label(EnterRoomFrame, text = "Enter Room ID", font = ("Arial",12,"bold"))
LabelIDEnter.grid(row = 0, column = 2)

entryIDenter = Entry(EnterRoomFrame)
entryIDenter.grid(row = 1, column = 2)

LabelUSEnter = Label(EnterRoomFrame, text = "Enter a username", font = ("Arial",12,"bold"))
LabelUSEnter.grid(row = 3, column = 2)

entryUSEnter = Entry(EnterRoomFrame)
entryUSEnter.grid(row = 4, column = 2)

buttonEnter = Button(EnterRoomFrame, text = "Enter", command = lambda: PLACEHOLDER())
buttonEnter.grid(row = 5, column = 2)

#CreateRoomFrame

LabelMakeIDCreate = Label(CreateRoomFrame, text = "Create Room ID", font = ("Arial",12,"bold"))
LabelMakeIDCreate.grid(row = 0, column = 2)

entryMakeIDCreate = Entry(CreateRoomFrame)
entryMakeIDCreate.grid(row = 1, column = 2)

LabelUSCreate = Label(CreateRoomFrame, text = "Create a username", font = ("Arial",12,"bold"))
LabelUSCreate.grid(row = 3, column = 2)

entryUSCreate = Entry(CreateRoomFrame)
entryUSCreate.grid(row = 4, column = 2)

buttonCreate = Button(CreateRoomFrame, text = "Create", command = lambda: PLACEHOLDER())
buttonCreate.grid(row = 5, column = 2)

#ChatRoomFrame

LabelTEST = Label(ChatRoomFrame, text = "text", font = ("Arial",100,"bold"))
LabelTEST.grid(row = 0, column = 0)

#MessageFrame

MessageEntry = Entry(ChatRoomFrame)
MessageEntry.grid(row = 2, column = 0)

MessageEnterButton = Button(ChatRoomFrame, text = "enter", command = lambda: xyz())
MessageEnterButton.grid(row = 2, column = 1)



#t1.start()
#t2.start()

root.mainloop()