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
        userbox.insert(END, '#Name of Passenger')
    elif str(user.get())=='ATTEN':
        userbox.delete(0, len(str(userbox.get())))
        userbox.insert(END, '#Name of Attendant')
    #elif str(user.get())=='ADMIN':
        #userbox.delete(0, len(str(userbox.get())))
        #userbox.insert(END, '#Admin Username')
def linked():
    #code for connecting databases and verification if the data inputted by the user matches up with the record stored in the tables.
    if str(user.get()) in ['STUPAR', 'ATTEN']  and str(passbox.get())!='' and str(userbox.get()) not in ['#Name of Passenger','#Name of Attendant']: #and other conditions as verification
        canvas.delete("all")
        canvas.create_window(260,80, window=tableselect)
        canvas.pack()
        canvas.create_window(260,130, window=PV)
        canvas.pack()
        canvas.create_window(260,180, window=lengthlabel)
        canvas.pack()
        lengthbox.insert(END, '#value from table')
        lengthbox['state']='disabled'
        canvas.create_window(260,200, window=lengthbox)
        canvas.pack()
        canvas.create_window(260,240, window=stopslabel)
        canvas.pack()
        stopsbox.insert(END, '#value from table')
        stopsbox['state']='disabled'
        canvas.create_window(260,260, window=stopsbox)
        canvas.pack()
        canvas.create_window(260,300, window=capacitylabel)
        canvas.pack()
        capacitybox.insert(END, '#value from table')
        capacitybox['state']='disabled'
        canvas.create_window(260,320, window=capacitybox)
        canvas.pack()
        canvas.create_window(500,180, window=attendantlabel)
        canvas.pack()
        attendantbox.insert(END, '#value from table')
        attendantbox['state']='disabled'
        canvas.create_window(500,200, window=attendantbox)
        canvas.pack()
        canvas.create_window(500,240, window=driverlabel)
        canvas.pack()
        driverbox.insert(END, '#value from table')
        driverbox['state']='disabled'
        canvas.create_window(500,260, window=driverbox)
        canvas.pack()
        canvas.create_window(500,300, window=conductorlabel)
        canvas.pack()
        conductorbox.insert(END, '#value from table')
        conductorbox['state']='disabled'
        canvas.create_window(500,320, window=conductorbox)
        canvas.pack()
        canvas.create_window(650,180, window=attenconlabel)
        canvas.pack()
        attenconbox.insert(END, '#value from table')
        attenconbox['state']='disabled'
        canvas.create_window(650,200, window=attenconbox)
        canvas.pack()
        canvas.create_window(650,240, window=driverconlabel)
        canvas.pack()
        driverconbox.insert(END, '#value from table')
        driverconbox['state']='disabled'
        canvas.create_window(650,260, window=driverconbox)
        canvas.pack()
        canvas.create_window(650,300, window=conconlabel)
        canvas.pack()
        conconbox.insert(END, '#value from table')
        conconbox['state']='disabled'
        canvas.create_window(650,320, window=conconbox)
        canvas.pack()
        if str(user.get()) == 'STUPAR':
            canvas.create_window(260,370, window=PASSENGER)
            canvas.pack()
            canvas.create_window(260,420, window=passidlabel)
            canvas.pack()
            passidbox.insert(END, '#value from table')
            passidbox['state']='disabled'
            canvas.create_window(260,450, window=passidbox)
            canvas.pack()
            canvas.create_window(260,490, window=namelabel)
            canvas.pack()
            namebox.insert(END, '#value from table')
            namebox['state']='disabled'
            canvas.create_window(260,510, window=namebox)
            canvas.pack()
            canvas.create_window(260,550, window=passpwdlabel)
            canvas.pack()
            passpwdbox.insert(END, '#value from table')
            passpwdbox['state']='disabled'
            canvas.create_window(260,570, window=passpwdbox)
            canvas.pack()
            canvas.create_window(260,610, window=phonelabel)
            canvas.pack()
            phonebox.insert(END, '#value from table')
            phonebox['state']='disabled'
            canvas.create_window(260,630, window=phonebox)
            canvas.pack()
            canvas.create_window(500,420, window=routelabel)
            canvas.pack()
            routebox.insert(END, '#value from table')
            routebox['state']='disabled'
            canvas.create_window(500,450, window=routebox)
            canvas.pack()
            canvas.create_window(500,490, window=stoplabel)
            canvas.pack()
            stopbox.insert(END, '#value from table')
            stopbox['state']='disabled'
            canvas.create_window(500,510, window=stopbox)
            canvas.pack()
        canvas.create_window(540,80, window=button2)
        canvas.pack()
        canvas.create_window(615,80, window=button3)
        canvas.pack()
        canvas.create_window(1000,280, window=map_widget)
        canvas.pack()
def routechange(event):
    PV['text']=str(table.get())
    canvas.update()
    canvas.pack()
def edit():
    button2['state']='disabled'
    if str(user.get()) == 'STUPAR':
        namebox['state']='normal'
        passpwdbox['state']='normal'
        phonebox['state']='normal'
        routebox['state']='normal'
        stopbox['state']='normal'
    elif str(user.get()) == 'ATTEN':
        lengthbox['state']='normal'
        stopsbox['state']='normal'
        capacitybox['state']='normal'
        attendantbox['state']='normal'
        driverbox['state']='normal'
        conductorbox['state']='normal'
        attenconbox['state']='normal'
        driverconbox['state']='normal'
        conconbox['state']='normal'
    button3['state']='normal'
def saveload():
    button3['state']='disabled'
    #will commit and push changes to main database, then pull it again
    if str(user.get()) == 'STUPAR':
        namebox['state']='disabled'
        passpwdbox['state']='disabled'
        phonebox['state']='disabled'
        routebox['state']='disabled'
        stopbox['state']='disabled'
    elif str(user.get()) == 'ATTEN':
        lengthbox['state']='disabled'
        stopsbox['state']='disabled'
        capacitybox['state']='disabled'
        attendantbox['state']='disabled'
        driverbox['state']='disabled'
        conductorbox['state']='disabled'
        attenconbox['state']='disabled'
        driverconbox['state']='disabled'
        conconbox['state']='disabled'
    button2['state']='normal'
########
canvas=Canvas(root, width=scr_w, height=scr_h, bg='white')
logoimg=PhotoImage(file='logoimage.png')
canvas.create_image(640,250, image=logoimg)
canvas.pack()
permit=ttk.Label(canvas, text="<WELCOME! YOU ARE:>", font=('Courier New',13), background='white')
canvas.create_window(240,460, window=permit)
canvas.pack()
user=StringVar()
stupar=tk.Radiobutton(canvas, text='A Student/Parent', font=('Courier New',11),variable=user, value='STUPAR', bg='white', command=permission)
canvas.create_window(240,490, window=stupar)
canvas.pack()
atten=tk.Radiobutton(canvas, text='An Attendant', font=('Courier New',11),variable=user, value='ATTEN', bg='white', command=permission)
canvas.create_window(222,510, window=atten)
canvas.pack()
#admin=tk.Radiobutton(canvas, text='An Administrator', font=('Courier New',11),variable=user, value='ADMIN', bg='white', command=permission)
#canvas.create_window(240,520, window=admin)
#canvas.pack()
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
routes=[]
routes.append('<Choose a route:>')
for i in range(1,23):
    x='PV-'+str(i)
    routes.append(x)
table=StringVar()
tableselect=ttk.Combobox(canvas, textvariable=table, font=('Courier New',11))
tableselect['values']=tuple(routes)
tableselect.state(["readonly"])
tableselect.current(0)
tableselect.bind("<<ComboboxSelected>>", routechange)
PV=ttk.Label(canvas, text=str(table.get()), font=('Courier New',15), background='white')
lengthlabel=ttk.Label(canvas, text='Length', font=('Courier New',11), background='white')
length=StringVar()
lengthbox=ttk.Entry(canvas, textvariable=length, font=('Courier New',9))
stopslabel=ttk.Label(canvas, text='Number of Stops', font=('Courier New',11), background='white')
stops=StringVar()
stopsbox=ttk.Entry(canvas, textvariable=stops, font=('Courier New',9))
capacitylabel=ttk.Label(canvas, text='Capacity', font=('Courier New',11), background='white')
capacity=StringVar()
capacitybox=ttk.Entry(canvas, textvariable=capacity, font=('Courier New',9))
attendantlabel=ttk.Label(canvas, text='Attendant', font=('Courier New',11), background='white')
attendantname=StringVar()
attendantbox=ttk.Entry(canvas, textvariable=attendantname, font=('Courier New',9))
attenconlabel=ttk.Label(canvas, text='Contact', font=('Courier New',11), background='white')
attencon=StringVar()
attenconbox=ttk.Entry(canvas, textvariable=attencon, font=('Courier New',9))
driverlabel=ttk.Label(canvas, text='Driver', font=('Courier New',11), background='white')
drivername=StringVar()
driverbox=ttk.Entry(canvas, textvariable=drivername, font=('Courier New',9))
driverconlabel=ttk.Label(canvas, text='Contact', font=('Courier New',11), background='white')
drivercon=StringVar()
driverconbox=ttk.Entry(canvas, textvariable=drivercon, font=('Courier New',9))
conductorlabel=ttk.Label(canvas, text='Conductor', font=('Courier New',11), background='white')
conductorname=StringVar()
conductorbox=ttk.Entry(canvas, textvariable=conductorname, font=('Courier New',9))
conconlabel=ttk.Label(canvas, text='Contact', font=('Courier New',11), background='white')
concon=StringVar()
conconbox=ttk.Entry(canvas, textvariable=concon, font=('Courier New',9))
PASSENGER=ttk.Label(canvas, text='Passenger Details', font=('Courier New',15), background='white')
passidlabel=ttk.Label(canvas, text='Passenger-ID', font=('Courier New',11), background='white')
passid=StringVar()
passidbox=ttk.Entry(canvas, textvariable=passid, font=('Courier New',9))
namelabel=ttk.Label(canvas, text='Name of Passenger', font=('Courier New',11), background='white')
name=StringVar()
namebox=ttk.Entry(canvas, textvariable=name, font=('Courier New',9))
passpwdlabel=ttk.Label(canvas, text='Password', font=('Courier New',11), background='white')
passpwd=StringVar()
passpwdbox=ttk.Entry(canvas, textvariable=passpwd, font=('Courier New',9))
phonelabel=ttk.Label(canvas, text='Phone Number', font=('Courier New',11), background='white')
phone=StringVar()
phonebox=ttk.Entry(canvas, textvariable=phone, font=('Courier New',9))
routelabel=ttk.Label(canvas, text='Route', font=('Courier New',11), background='white')
route=StringVar()
routebox=ttk.Entry(canvas, textvariable=route, font=('Courier New',9))
stoplabel=ttk.Label(canvas, text='Stop', font=('Courier New',11), background='white')
stop=StringVar()
stopbox=ttk.Entry(canvas, textvariable=stop, font=('Courier New',9))
button2=ttk.Button(canvas, text='🖉', command=edit)
button3=ttk.Button(canvas, text='💾', command=saveload, state='disabled')
map_widget=tmap.TkinterMapView(canvas, width=400, height=400, corner_radius=0)
map_widget.set_position(28.597055209685127, 77.2266516760437)
map_widget.set_zoom(12)
########
#------map coordinates and stops-------#
spv=map_widget.set_marker(28.597055209685127, 77.2266516760437, text="SPV")
#pv1
saketj=map_widget.set_marker(28.52211, 77.21593, text="Saket J Block")
saketh=map_widget.set_marker(28.5223, 77.212, text="Saket H Block")
gyan=map_widget.set_marker(28.52573,77.20557, text="Gyan Bharti School")
shivalik=map_widget.set_marker(28.52784,77.20598, text="Shivalik Colony")
malv1=map_widget.set_marker(28.53613, 77.20901, text="Malviya Nagar 1")
sarv=map_widget.set_marker(28.54361, 77.20763, text="Sarvpriya Vihar")
swami=map_widget.set_marker(28.54219, 77.22594, text="Swami Nagar")
tito=map_widget.set_marker(28.54608,77.22969, text="Josip Broz Tito Marg")
sadiq=map_widget.set_marker(28.5542,77.22821, text="Sadiq Nagar")
hudco=map_widget.set_marker(28.56037,77.23096, text="Hudco Place")
andrew=map_widget.set_marker(28.56555,77.23396, text="Andrews Ganj")
pv1= map_widget.set_path([saketj.position,saketh.position,gyan.position,shivalik.position,malv1.position,sarv.position,swami.position,tito.position,sadiq.position,hudco.position,andrew.position,spv.position])
#pv9
kalka=map_widget.set_marker(28.52941,77.25234, text="DDA Flats Kalkaji")
manda=map_widget.set_marker(28.53295,77.25315, text="Mandakini Enclave")
shivap=map_widget.set_marker(28.53353,77.25449, text="Shivalik Apartments")
crmark2=map_widget.set_marker(28.53613,77.2535, text="C.R. Park Market No. 2")
mela=map_widget.set_marker(28.53799,77.25221, text="Mela Ground")
crmark1=map_widget.set_marker(28.53998,77.24855, text="C.R. Park Market No. 1")
crk=map_widget.set_marker(28.54026, 77.24373, text="C.R. Park K Block")
cra=map_widget.set_marker(28.543,77.24239, text="C.R. Park A Block")
defence=map_widget.set_marker(28.57488,77.2385, text="Defence Colony")
pv9= map_widget.set_path([kalka.position,manda.position,shivap.position,crmark2.position,mela.position,crmark1.position,crk.position,cra.position,defence.position,spv.position])
#pv20
guj=map_widget.set_marker(28.64363,77.29127, text="Gujarat Vihar")
swasth=map_widget.set_marker(28.64038,77.28629, text="Swasthya Vihar")
walia=map_widget.set_marker(28.63283, 77.28072, text="Walia Nursing Home")
pv20= map_widget.set_path([guj.position,swasth.position,walia.position,spv.position])
###
root.mainloop()
