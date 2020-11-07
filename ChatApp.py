from tkinter import *
from tkinter import messagebox
from time import localtime, strftime, time
from Firebase import PyFirebase as PyFB

db = PyFB('./certification.json', 'https://python-steve28.firebaseio.com/')
room = 'testroom'

test = Tk()
test.geometry('400x500+0+0')
test.resizable(False, False)

listbox = Listbox(test, selectmode='extended', width=53, height=20)
textinput = Entry(test, width=33)
nameinput = Entry(test, width=7)

def sendserver(value, name, roomname):
    nowtime = strftime('%Y-%m-%d %H:%M:%S', localtime(time()))
    data = [nowtime, name, value]
    v = db.GetValue(roomname) if db.GetValue(roomname) else []
    v.append(data)
    db.Update(roomname, v)

def send(event=""):
    value = textinput.get()
    name = nameinput.get()
    if value == "" or name == "":
        messagebox.showerror("title", "error")
    else:
        sendserver(value, name, room)

sendbtn = Button(test, text="SEND", command=send, width=7)
textinput.bind('<Return>', send)

listbox.place(x=10, y=10)
textinput.place(x=70, y=370)
nameinput.place(x=10, y=370)
sendbtn.place(x=320, y=370)

def updateItem(data):
    print("updating!")
    listbox.delete(0, -1)
    for i in data:
        listbox.insert(0, *data)

def listener(ev):
    d = ev.data
    print(d)
    if d: updateItem(d[room])

db.AddListener('', listener)
test.mainloop()
