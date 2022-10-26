from tkinter import *
from tkinter import ttk
import tkinter as tk
import tkintermapview as tmap
import time
import os
########
root=Tk()
root.resizable(width=False, height=False)
root.title('SPVTransit')
root.configure(bg='white')
root.state('zoomed')
global scr_w
scr_w=root.winfo_screenwidth()
global scr_h
scr_h=root.winfo_screenheight()
root.geometry(str(scr_w)+'x'+str(scr_h))
########
def permission():
    if str(user.get())=='STUPAR':
        userbox.delete(0, len(str(userbox.get())))
        userbox.insert(END, '#Name of Parent')
    elif str(user.get())=='ATTEN':
        userbox.delete(0, len(str(userbox.get())))
        userbox.insert(END, '#Name of Attendant')
    elif str(user.get())=='ADMIN':
        userbox.delete(0, len(str(userbox.get())))
        userbox.insert(END, '#Admin Username')
def linked():
    #code for connecting databases and verification if the data inputted by the user matches up with the record stored in the tables.
    canvas.delete("all")
    
########
canvas=Canvas(root, width=scr_w, height=scr_h, bg='white')
logoimg=PhotoImage(file='logoimage.png')
canvas.create_image(640,250, image=logoimg)
canvas.pack()
permit=ttk.Label(canvas, text="<WELCOME! YOU ARE:>", font=('Courier New',13), background='white')
canvas.create_window(240,450, window=permit)
canvas.pack()
user=StringVar()
stupar=tk.Radiobutton(canvas, text='A Student/Parent', font=('Courier New',11),variable=user, value='STUPAR', bg='white', command=permission)
canvas.create_window(240,480, window=stupar)
canvas.pack()
atten=tk.Radiobutton(canvas, text='An Attendant', font=('Courier New',11),variable=user, value='ATTEN', bg='white', command=permission)
canvas.create_window(222,500, window=atten)
canvas.pack()
admin=tk.Radiobutton(canvas, text='An Administrator', font=('Courier New',11),variable=user, value='ADMIN', bg='white', command=permission)
canvas.create_window(240,520, window=admin)
canvas.pack()
uname=StringVar()
passwd=StringVar()
userlabel=ttk.Label(canvas, text="<Username:>", font=('Courier New',10), background='white')
canvas.create_window(640,450, window=userlabel)
canvas.pack()
userbox=ttk.Entry(canvas, textvariable=uname, font=('Courier New',11))
canvas.create_window(640,470, window=userbox)
canvas.pack()
passlabel=ttk.Label(canvas, text="<Password:>", font=('Courier New',10), background='white')
canvas.create_window(640,500, window=passlabel)
canvas.pack()
passbox=ttk.Entry(canvas, textvariable=passwd, font=('Courier New',11), show="*")
canvas.create_window(640,520, window=passbox)
canvas.pack()
proceed=ttk.Label(canvas, text="   <Verify and \n Connect Databases:>", font=('Courier New',10), background='white')
canvas.create_window(1040,470, window=proceed)
canvas.pack()
button1=ttk.Button(canvas, text='>', command=linked)
canvas.create_window(1040,510, window=button1)
canvas.pack()
########
root.mainloop()
