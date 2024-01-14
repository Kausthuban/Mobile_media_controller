import tkinter
from tkinter import filedialog
from adb import *
from tkinter import *
from tkinter import  messagebox
curr_path = getpath()
changepath()
global x
x=0
root = Tk()
root.title("Media Controller")
root.configure(background='black')


def change_frame():
    connection.grid_forget()
    Media.grid_forget()
    if win.get()==0:
        connection.grid(row=2,column=0,columnspan=3)
    if win.get()==1:
        Media.grid(row=2,column=0,columnspan=3)


# Root buttons
win = IntVar()
win.set(0)
Radiobutton(root,text="Control",variable=win,value=1,command=change_frame,bg='black',fg='white',activebackground='black',activeforeground='black',selectcolor='black').grid(row=0,column=1)
Radiobutton(root,text="Connect",variable=win,value=0,command=change_frame,bg='black',fg='white',activebackground='black',activeforeground='black',selectcolor='black').grid(row=0,column=0)




#Connection Frame
global connection
connection = LabelFrame(root,text="Connection",padx=5,pady=5,bg='black',fg='white')
def disable_pin(val):
    global pair_button,pin_val
    pair_button.grid_forget()
    global pin_val
    pin_val.grid_forget()
    if val==0:
        pair_button = Button(connection,text="Connect",bg='black',fg='white',command=lambda : connect(ip_val.get(),port_val.get()))
    if val == 1:
        pin_val = Entry(connection, bg='black', fg='white', insertbackground='white')
        pin_val.config(state="normal")
        pair_button = Button(connection, text="Pair",bg='black',fg='white',command=lambda : pair(ip_val.get(),port_val.get(),pin_val.get()))
        pin_val.grid(row=3, column=1, columnspan=2)

    pair_button.grid(row=4, column=1)
pin = IntVar()

Radiobutton(connection,text="Pair",variable=pin,value=1,command=lambda : disable_pin(pin.get()),bg='black',fg='white',activebackground='black',activeforeground='black',selectcolor='black').grid(row=0,column=1)
Radiobutton(connection,text="Connect",variable=pin,value=0,command=lambda : disable_pin(pin.get()),bg='black',fg='white',activebackground='black',activeforeground='black',selectcolor='black').grid(row=0,column=0)

ip_txt = Label(connection,text="IP address : ",bg='black',fg='white')
ip_val = Entry(connection,bg='black',fg='white',insertbackground='white')
ip_txt.grid(row=1,column=0)
ip_val.grid(row=1,column=1,columnspan=2)

port_txt = Label(connection,text="Port Number : ",bg='black',fg='white')
port_val = Entry(connection,bg='black',fg='white',insertbackground='white')
port_txt.grid(row=2,column=0)
port_val.grid(row=2,column=1,columnspan=2)

pin_txt = Label(connection,text="Pin Number : ",bg='black',fg='white')
pin_val = Entry(connection,bg='black',fg='white',insertbackground='white')
pin_txt.grid(row=3,column=0)
# pin_val.grid(row=3,column=1,columnspan=2)

pair_button = Button(connection,text="Pair",bg='black',fg='white')

pair_button.grid(row=4,column=1)

connection.grid(row=2,column=0,columnspan=3)



# Media Frame

global Media
Media = LabelFrame(root,text="Media Control",padx=5,pady=5,bg='black',fg='white')

prev = PhotoImage(file=curr_path+r'\prev.png')
play = PhotoImage(file=curr_path+r'\pause.png')
stop = PhotoImage(file=curr_path+r'\stop.png')
next = PhotoImage(file=curr_path+r'\next.png')

def pause_play_event(value,x):
    x=x^1
    event = send_event(value)
    if event != None:
        messagebox.showwarning("Connection Error","Device Not Connected")

    global play_btn
    play_btn.grid_forget()
    if x==0:
        play_btn = Button(Media,image=play,command=lambda :pause_play_event(85,x),pady=30,padx=30)
    if x==1:
        play_btn = Button(Media,image=stop,command=lambda :pause_play_event(85,x),pady=30,padx=30)
    play_btn.grid(row=0, column=2)

def key_event(value):
    event = send_event(value)
    if event != None:
        messagebox.showwarning("Connection Error", "Device Not Connected")

prev_btn = Button(Media,image=prev,command=lambda :key_event(88),pady=30,padx=30)
play_btn = Button(Media,image=play,command=lambda :pause_play_event(85,x),pady=30,padx=30)
next_btn = Button(Media,image=next,command=lambda :key_event(87),pady=30,padx=30)

prev_btn.grid(row=0,column=0)
play_btn.grid(row=0,column=2)
next_btn.grid(row=0,column=4)


Media.configure(background='black')
connection.configure(background='black')

# statusbar
stat = "Disconnected"
if conn_stat():
    stat = "Device connected"
else:
    stat = "Disconnected"
status = Label(root,text=stat,bg='black',fg='white')
status.grid(row=5,column=0,sticky=W+E)
mainloop()