#---imported libraries---#

from tkinter import *
from tkinter import ttk
import tkinter as tk
import tkintermapview as tmap
import time
import os

#---window creation---#

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

#---functions---#

def permission(): #Generates prompt to input in username entry widget.
    if str(user.get())=='STUPAR':
        userbox.delete(0, len(str(userbox.get())))
        userbox.insert(END, '#Name of Passenger')
    elif str(user.get())=='ATTEN':
        userbox.delete(0, len(str(userbox.get())))
        userbox.insert(END, '#Name of Attendant')
    #elif str(user.get())=='ADMIN':
        #userbox.delete(0, len(str(userbox.get())))
        #userbox.insert(END, '#Admin Username')
        
def linked(): #moves the user to the data screen
    #code for connecting databases and verification if the data inputted by the user matches up with the record stored in the tables.
    
    if str(user.get()) in ['STUPAR', 'ATTEN']  and str(passbox.get())!='' and str(userbox.get()) not in ['#Name of Passenger','#Name of Attendant']:
        #and other conditions as verification

        canvas.delete("all")
        
        canvas.create_window(260,80, window=tableselect) #Places route choice combobox widget
        canvas.pack()
        
        canvas.create_window(260,130, window=PV) #Places label for route name
        canvas.pack()
        
        canvas.create_window(260,180, window=lengthlabel) #Places label and table entry for route length
        canvas.pack()
        lengthbox.insert(END, '#value from table')
        lengthbox['state']='disabled'
        canvas.create_window(260,200, window=lengthbox)
        canvas.pack()
        
        canvas.create_window(260,240, window=stopslabel) #Places label and table entry for no. of stops
        canvas.pack()
        stopsbox.insert(END, '#value from table')
        stopsbox['state']='disabled'
        canvas.create_window(260,260, window=stopsbox)
        canvas.pack()
        
        canvas.create_window(260,300, window=capacitylabel) #Places label and table entry for capacity
        canvas.pack()
        capacitybox.insert(END, '#value from table')
        capacitybox['state']='disabled'
        canvas.create_window(260,320, window=capacitybox)
        canvas.pack()
        
        canvas.create_window(500,180, window=attendantlabel) #Places label and table entry for the attendant of that route
        canvas.pack()
        attendantbox.insert(END, '#value from table')
        attendantbox['state']='disabled'
        canvas.create_window(500,200, window=attendantbox)
        canvas.pack()
        
        canvas.create_window(500,240, window=driverlabel) #Places label and table entry for the driver of that route
        canvas.pack()
        driverbox.insert(END, '#value from table')
        driverbox['state']='disabled'
        canvas.create_window(500,260, window=driverbox)
        canvas.pack()
        
        canvas.create_window(500,300, window=conductorlabel)#Places label and table entry for the conductor of that route
        canvas.pack()
        conductorbox.insert(END, '#value from table')
        conductorbox['state']='disabled'
        canvas.create_window(500,320, window=conductorbox)
        canvas.pack()
        
        canvas.create_window(650,180, window=attenconlabel) #Places label and table entry for the attendant's contact
        canvas.pack()
        attenconbox.insert(END, '#value from table')
        attenconbox['state']='disabled'
        canvas.create_window(650,200, window=attenconbox)
        canvas.pack()
        
        canvas.create_window(650,240, window=driverconlabel)#Places label and table entry for the drivers's contact
        canvas.pack()
        driverconbox.insert(END, '#value from table')
        driverconbox['state']='disabled'
        canvas.create_window(650,260, window=driverconbox)
        canvas.pack()
        
        canvas.create_window(650,300, window=conconlabel) #Places label and table entry for the conductor's contact
        canvas.pack()
        conconbox.insert(END, '#value from table')
        conconbox['state']='disabled'
        canvas.create_window(650,320, window=conconbox)
        canvas.pack()

        canvas.create_window(540,80, window=button2)#places edit button
        canvas.pack()
        
        canvas.create_window(615,80, window=button3)#places save button
        canvas.pack()
        
        canvas.create_window(1000,280, window=map_widget)#places map widget
        canvas.pack()

        canvas.create_window(1000,510, window=stopnamelabel) #Places label for name of stop
        canvas.pack()

        canvas.create_window(890,560, window=xlabel) #Places label and table entry for the stop's latitude
        canvas.pack()
        xbox.insert(END, '#select a stop')
        xbox['state']='disabled'
        canvas.create_window(890, 580, window=xbox)
        canvas.pack()

        canvas.create_window(1130,560, window=ylabel) #Places label and table entry for the stop's longitude
        canvas.pack()
        ybox.insert(END, '#select a stop')
        ybox['state']='disabled'
        canvas.create_window(1130, 580, window=ybox)
        canvas.pack()

        canvas.create_window(890,620, window=numpasslabel) #Places label and table entry for the number of passengers
        canvas.pack()
        numpassbox.insert(END, '#value from table')
        numpassbox['state']='disabled'
        canvas.create_window(890,640, window=numpassbox)
        canvas.pack()

        canvas.create_window(1130,620, window=timelabel) #Places label and table entry for the number of passengers
        canvas.pack()
        timebox.insert(END, '#value from table')
        timebox['state']='disabled'
        canvas.create_window(1130,640, window=timebox)
        canvas.pack()
        

        #canvas.create_image(1000,61, image=pinimg)#Places a small pin on top pf the map 
        #canvas.pack()

        ##Above were the windows generated for all users
    
        if str(user.get()) == 'STUPAR':
            
            canvas.create_window(260,370, window=PASSENGER) #Places label for passenger details
            canvas.pack()
            
            canvas.create_window(260,420, window=passidlabel) #Places label and table entry for the passenger ID
            canvas.pack()
            passidbox.insert(END, '#value from table')
            passidbox['state']='disabled'
            canvas.create_window(260,450, window=passidbox)
            canvas.pack()
            
            canvas.create_window(260,490, window=namelabel)#Places label and table entry for the passenger's name
            canvas.pack()
            namebox.insert(END, '#value from table')
            namebox['state']='disabled'
            canvas.create_window(260,510, window=namebox)
            canvas.pack()
            
            canvas.create_window(260,550, window=passpwdlabel)#Places label and table entry for the passenger's password
            canvas.pack()
            passpwdbox.insert(END, '#value from table')
            passpwdbox['state']='disabled'
            canvas.create_window(260,570, window=passpwdbox)
            canvas.pack()
            
            canvas.create_window(260,610, window=phonelabel)#Places label and table entry for the passenger's phone number
            canvas.pack()
            phonebox.insert(END, '#value from table')
            phonebox['state']='disabled'
            canvas.create_window(260,630, window=phonebox)
            canvas.pack()
            
            canvas.create_window(500,420, window=routelabel)#Places label and table entry for the passenger's route
            canvas.pack()
            routebox.insert(END, '#value from table')
            routebox['state']='disabled'
            canvas.create_window(500,450, window=routebox)
            canvas.pack()
            
            canvas.create_window(500,490, window=stoplabel)#Places label and table entry for the passenger's stop
            canvas.pack()
            stopbox.insert(END, '#value from table')
            stopbox['state']='disabled'
            canvas.create_window(500,510, window=stopbox)
            canvas.pack()


def routechange(event): #updates to new route
    global pv1, pv2, pv5, pv9, pv20up
    PV['text']=str(table.get())
    pv1.delete()
    pv2.delete()
    pv5.delete()
    pv9.delete()
    pv20up.delete()
    if str(table.get())[3::]=='1':
        pv1= map_widget.set_path([saketj.position,saketh.position,gyan.position,shivalik.position,malv1.position,sarv.position,swami.position,tito.position,sadiq.position,hudco.position,andrew.position,spv.position])
    elif str(table.get())[3::]=='2':
        pv2=map_widget.set_path([dda.position,jnu.position,ber.position,munmark.position,rkp.position,iit.position,saf.position,gp1.position,kid.position,jorb.position,spv.position])
    elif str(table.get())[3::]=='5':
        pv5=map_widget.set_path([sch.position,sksii.position,ski.position,hk1.position,asi.position,gul.position,nee.position,ayu.position,shi.position,spv.position])
    elif str(table.get())[3::]=='9':
        pv9= map_widget.set_path([kalka.position,manda.position,shivap.position,crmark2.position,mela.position,crmark1.position,crk.position,cra.position,defence.position,spv.position])
    elif str(table.get())[3::]=='20':
        pv20up= map_widget.set_path([guj.position,swasth.position,walia.position,spv.position])
    else:
        pass
    canvas.update()
    canvas.pack()

    
def edit(): #allows user to edit respective data by enabling the disabled entry boxes
    button2['state']='disabled'
    
    if str(user.get()) == 'STUPAR': #passenger can only edit their own data
        namebox['state']='normal'
        passpwdbox['state']='normal'
        phonebox['state']='normal'
        routebox['state']='normal'
        stopbox['state']='normal'
        
    elif str(user.get()) == 'ATTEN': #attendant can edit some data from routes
        lengthbox['state']='normal'
        stopsbox['state']='normal'
        capacitybox['state']='normal'
        attendantbox['state']='normal'
        driverbox['state']='normal'
        conductorbox['state']='normal'
        attenconbox['state']='normal'
        driverconbox['state']='normal'
        conconbox['state']='normal'
        numpassbox['state']='normal'
        
    button3['state']='normal'
    
def saveload(): #will commit and push changes to main database, then pull it again
    
    #code to save and load
    
    button3['state']='disabled'
    
    if str(user.get()) == 'STUPAR': #data is no longer editable. press edit button to change again
        namebox['state']='disabled'
        passpwdbox['state']='disabled'
        phonebox['state']='disabled'
        routebox['state']='disabled'
        stopbox['state']='disabled'
        
    elif str(user.get()) == 'ATTEN': #data is no longer editable. press edit button to change again
        lengthbox['state']='disabled'
        stopsbox['state']='disabled'
        capacitybox['state']='disabled'
        attendantbox['state']='disabled'
        driverbox['state']='disabled'
        conductorbox['state']='disabled'
        attenconbox['state']='disabled'
        driverconbox['state']='disabled'
        conconbox['state']='disabled'
        numpassbox['state']='normal'
        
    button2['state']='normal'

def stopclick(marker): #Function for displaying info when a stop is clicked
    xbox['state']='normal'
    xbox.delete(0, len(str(xbox.get())))
    xbox.insert(END, str(marker.position[0]))
    xbox['state']='disabled'

    ybox['state']='normal'
    ybox.delete(0, len(str(ybox.get())))
    ybox.insert(END, str(marker.position[1]))
    ybox['state']='disabled'

    stopnamelabel['text']=marker.text
#---widget creation---#
    
canvas=Canvas(root, width=scr_w, height=scr_h, bg='white') #Generates canvas to draw the widgets onto

logoimg=PhotoImage(file='logoimage.png')
#pinimg=PhotoImage(file='pin.png')

canvas.create_image(640,250, image=logoimg) #creates logo image and draws it on the canvas
canvas.pack()

permit=ttk.Label(canvas, text="<WELCOME! YOU ARE:>", font=('Courier New',13), background='white') #widget above permissions
canvas.create_window(240,460, window=permit)
canvas.pack()

#Note: all StringVar() values store the values passed to Entries/radiobuttons/comboboxes as a texvariable

user=StringVar()
stupar=tk.Radiobutton(canvas, text='A Student/Parent', font=('Courier New',11),variable=user, value='STUPAR', bg='white', command=permission) #passenger option
canvas.create_window(240,490, window=stupar)
canvas.pack()

atten=tk.Radiobutton(canvas, text='An Attendant', font=('Courier New',11),variable=user, value='ATTEN', bg='white', command=permission) #attendant option
canvas.create_window(222,510, window=atten)
canvas.pack()

#admin=tk.Radiobutton(canvas, text='An Administrator', font=('Courier New',11),variable=user, value='ADMIN', bg='white', command=permission)
#canvas.create_window(240,520, window=admin)
#canvas.pack()

uname=StringVar()
passwd=StringVar()

userlabel=ttk.Label(canvas, text="<Username:>", font=('Courier New',10), background='white') #label for username
canvas.create_window(640,450, window=userlabel)
canvas.pack()

userbox=ttk.Entry(canvas, textvariable=uname, font=('Courier New',11)) #entry for username
canvas.create_window(640,470, window=userbox)
canvas.pack()

passlabel=ttk.Label(canvas, text="<Password:>", font=('Courier New',10), background='white') #label for password
canvas.create_window(640,500, window=passlabel)
canvas.pack()

passbox=ttk.Entry(canvas, textvariable=passwd, font=('Courier New',11), show="*") #entry for password
canvas.create_window(640,520, window=passbox)
canvas.pack()

proceed=ttk.Label(canvas, text="   <Verify and \n Connect Databases:>", font=('Courier New',10), background='white') #widget above proceed button
canvas.create_window(1040,470, window=proceed)
canvas.pack()

button1=ttk.Button(canvas, text='>', command=linked) #proceed button
canvas.create_window(1040,510, window=button1)
canvas.pack()

routes=[] #generates PV-1 to PV-22
routes.append('<Choose a route:>')
for i in range(1,23):
    q='PV-'+str(i)
    routes.append(q)

table=StringVar()
tableselect=ttk.Combobox(canvas, textvariable=table, font=('Courier New',11)) #Creates Combobox with route options
tableselect['values']=tuple(routes)
tableselect.state(["readonly"])
tableselect.current(0)
tableselect.bind("<<ComboboxSelected>>", routechange)

PV=ttk.Label(canvas, text=str(table.get()), font=('Courier New',15), background='white') #label showing current route number

lengthlabel=ttk.Label(canvas, text='Length', font=('Courier New',11), background='white') #label and entry showing current route length
length=StringVar()
lengthbox=ttk.Entry(canvas, textvariable=length, font=('Courier New',9))

stopslabel=ttk.Label(canvas, text='Number of Stops', font=('Courier New',11), background='white') #label and entry showing stops on route
stops=StringVar()
stopsbox=ttk.Entry(canvas, textvariable=stops, font=('Courier New',9))

capacitylabel=ttk.Label(canvas, text='Capacity', font=('Courier New',11), background='white') #label and entry showing capacity
capacity=StringVar()
capacitybox=ttk.Entry(canvas, textvariable=capacity, font=('Courier New',9)) 

attendantlabel=ttk.Label(canvas, text='Attendant', font=('Courier New',11), background='white')#label and entry showing attendant
attendantname=StringVar()
attendantbox=ttk.Entry(canvas, textvariable=attendantname, font=('Courier New',9))

attenconlabel=ttk.Label(canvas, text='Contact', font=('Courier New',11), background='white')#label and entry showing attendant contact
attencon=StringVar()
attenconbox=ttk.Entry(canvas, textvariable=attencon, font=('Courier New',9))

driverlabel=ttk.Label(canvas, text='Driver', font=('Courier New',11), background='white')#label and entry showing driver
drivername=StringVar()
driverbox=ttk.Entry(canvas, textvariable=drivername, font=('Courier New',9))

driverconlabel=ttk.Label(canvas, text='Contact', font=('Courier New',11), background='white')#label and entry showing driver contact
drivercon=StringVar()
driverconbox=ttk.Entry(canvas, textvariable=drivercon, font=('Courier New',9))

conductorlabel=ttk.Label(canvas, text='Conductor', font=('Courier New',11), background='white')#label and entry showing conductor
conductorname=StringVar()
conductorbox=ttk.Entry(canvas, textvariable=conductorname, font=('Courier New',9))

conconlabel=ttk.Label(canvas, text='Contact', font=('Courier New',11), background='white')#label and entry showing conductor conatact
concon=StringVar()
conconbox=ttk.Entry(canvas, textvariable=concon, font=('Courier New',9))

PASSENGER=ttk.Label(canvas, text='Passenger Details', font=('Courier New',15), background='white') #header widget for passenger details

passidlabel=ttk.Label(canvas, text='Passenger-ID', font=('Courier New',11), background='white')#label and entry showing passenger ID
passid=StringVar()
passidbox=ttk.Entry(canvas, textvariable=passid, font=('Courier New',9))

namelabel=ttk.Label(canvas, text='Name of Passenger', font=('Courier New',11), background='white')#label and entry showing passenger name
name=StringVar()
namebox=ttk.Entry(canvas, textvariable=name, font=('Courier New',9))

passpwdlabel=ttk.Label(canvas, text='Password', font=('Courier New',11), background='white')#label and entry showing passenger password
passpwd=StringVar()
passpwdbox=ttk.Entry(canvas, textvariable=passpwd, font=('Courier New',9))

phonelabel=ttk.Label(canvas, text='Phone Number', font=('Courier New',11), background='white')#label and entry showing passenger phone number
phone=StringVar()
phonebox=ttk.Entry(canvas, textvariable=phone, font=('Courier New',9))

routelabel=ttk.Label(canvas, text='Route', font=('Courier New',11), background='white')#label and entry showing passenger's route
route=StringVar()
routebox=ttk.Entry(canvas, textvariable=route, font=('Courier New',9))

stoplabel=ttk.Label(canvas, text='Stop', font=('Courier New',11), background='white')#label and entry showing passenger's stop
stop=StringVar()
stopbox=ttk.Entry(canvas, textvariable=stop, font=('Courier New',9))

stopnamelabel=ttk.Label(canvas, text='<Select a Stop:>', font=('Courier New',15), background='white') #label showing selected stop/prompts the user to select one

xlabel=ttk.Label(canvas, text='Latitude', font=('Courier New',11), background='white')#label and entry showing latitude 
x=StringVar()
xbox=ttk.Entry(canvas, textvariable=x, font=('Courier New',9))

ylabel=ttk.Label(canvas, text='Longitude', font=('Courier New',11), background='white')#label and entry showing longitude
y=StringVar()
ybox=ttk.Entry(canvas, textvariable=y, font=('Courier New',9))

numpasslabel=ttk.Label(canvas, text='Number of Passengers', font=('Courier New',11), background='white')#label and entry showing no. of passengers
numpass=StringVar()
numpassbox=ttk.Entry(canvas, textvariable=numpass, font=('Courier New',9))

timelabel=ttk.Label(canvas, text='Time of Arrival', font=('Courier New',11), background='white')#label and entry showing route a stop belongs to
time=StringVar()
timebox=ttk.Entry(canvas, textvariable=time, font=('Courier New',9))

button2=ttk.Button(canvas, text='🖉', command=edit) #edit button
button3=ttk.Button(canvas, text='💾', command=saveload, state='disabled') #save and load button

map_widget=tmap.TkinterMapView(canvas, width=400, height=400, corner_radius=5) #map widget

#---map options, coordinates and stops---#

map_widget.set_position(28.597055209685127, 77.2266516760437)
map_widget.set_zoom(14)
spv=map_widget.set_marker(28.597055209685127, 77.2266516760437, command=stopclick, text="SPV", font=('Courier New',15))
#pv1
saketj=map_widget.set_marker(28.52211, 77.21593, command=stopclick, text="Saket J Block", font=('Courier New',9), marker_color_circle='white', marker_color_outside='purple', text_color='black')
saketh=map_widget.set_marker(28.5223, 77.212, command=stopclick, text="Saket H Block", font=('Courier New',9), marker_color_circle='white', marker_color_outside='purple', text_color='black')
gyan=map_widget.set_marker(28.52573,77.20557, command=stopclick,text="Gyan Bharti School", font=('Courier New',9), marker_color_circle='white', marker_color_outside='purple', text_color='black')
shivalik=map_widget.set_marker(28.52784,77.20598, command=stopclick, text="Shivalik Colony", font=('Courier New',9), marker_color_circle='white', marker_color_outside='purple', text_color='black')
malv1=map_widget.set_marker(28.53613, 77.20901, command=stopclick, text="Malviya Nagar 1", font=('Courier New',9), marker_color_circle='white', marker_color_outside='purple', text_color='black')
sarv=map_widget.set_marker(28.54361, 77.20763, command=stopclick,text="Sarvpriya Vihar", font=('Courier New',9), marker_color_circle='white', marker_color_outside='purple', text_color='black')
swami=map_widget.set_marker(28.54219, 77.22594,command=stopclick, text="Swami Nagar", font=('Courier New',9), marker_color_circle='white', marker_color_outside='purple', text_color='black')
tito=map_widget.set_marker(28.54608,77.22969,command=stopclick, text="Josip Broz Tito Marg", font=('Courier New',9), marker_color_circle='white', marker_color_outside='purple', text_color='black')
sadiq=map_widget.set_marker(28.5542,77.22821,command=stopclick, text="Sadiq Nagar", font=('Courier New',9), marker_color_circle='white', marker_color_outside='purple', text_color='black')
hudco=map_widget.set_marker(28.56037,77.23096,command=stopclick, text="Hudco Place", font=('Courier New',9), marker_color_circle='white', marker_color_outside='purple', text_color='black')
andrew=map_widget.set_marker(28.56555,77.23396,command=stopclick, text="Andrews Ganj", font=('Courier New',9), marker_color_circle='white', marker_color_outside='purple', text_color='black')
pv1= map_widget.set_path([saketj.position,saketh.position,gyan.position,shivalik.position,malv1.position,sarv.position,swami.position,tito.position,sadiq.position,hudco.position,andrew.position,spv.position])
#pv2
dda=map_widget.set_marker(28.55627,77.17526,command=stopclick, text="DDA Flats Munirka", font=('Courier New',9), marker_color_circle='white', marker_color_outside='orange', text_color='black')
jnu=map_widget.set_marker(28.535,77.16933,command=stopclick, text="JNU", font=('Courier New',9), marker_color_circle='white', marker_color_outside='orange', text_color='black')
ber=map_widget.set_marker(28.55166,77.18212,command=stopclick, text="Ber Sarai", font=('Courier New',9), marker_color_circle='white', marker_color_outside='orange', text_color='black')
munmark=map_widget.set_marker(28.55469,77.17767,command=stopclick, text="Munirka Market", font=('Courier New',9), marker_color_circle='white', marker_color_outside='orange', text_color='black')
rkp=map_widget.set_marker(28.54888,77.18754,command=stopclick, text="RK Puram Sector III", font=('Courier New',9), marker_color_circle='white', marker_color_outside='orange', text_color='black')
iit=map_widget.set_marker(28.54602,77.19609,command=stopclick, text="IIT Gate", font=('Courier New',9), marker_color_circle='white', marker_color_outside='orange', text_color='black')
saf=map_widget.set_marker(28.55312,77.20155,command=stopclick, text="Safdarjung Development Area", font=('Courier New',9), marker_color_circle='white', marker_color_outside='orange', text_color='black')
gp1=map_widget.set_marker(28.56025,77.20341,command=stopclick, text="Green Park", font=('Courier New',9), marker_color_circle='white', marker_color_outside='orange', text_color='black')
kid=map_widget.set_marker(28.57275,77.20922,command=stopclick, text="Kidwai Nagar", font=('Courier New',9), marker_color_circle='white', marker_color_outside='orange', text_color='black')
jorb=map_widget.set_marker(28.58579,77.21262,command=stopclick, text="Jor Bagh", font=('Courier New',9), marker_color_circle='white', marker_color_outside='orange', text_color='black')
pv2= map_widget.set_path([dda.position,jnu.position,ber.position,munmark.position,rkp.position,iit.position,saf.position,gp1.position,kid.position,jorb.position,spv.position])
#pv5
sch=map_widget.set_marker(28.52911,77.21406,command=stopclick, text="Saket City Hospital", font=('Courier New',9), marker_color_circle='white', marker_color_outside='green', text_color='black')
sksii=map_widget.set_marker(28.53353,77.23202,command=stopclick, text="Sheikh Sarai II", font=('Courier New',9), marker_color_circle='white', marker_color_outside='green', text_color='black')
ski=map_widget.set_marker(28.53845,77.22284,command=stopclick, text="Sheikh Sarai I", font=('Courier New',9), marker_color_circle='white', marker_color_outside='green', text_color='black')
hk1=map_widget.set_marker(28.54911,77.21011,command=stopclick, text="Hauz Khas I", font=('Courier New',9), marker_color_circle='white', marker_color_outside='green', text_color='black')
asi=map_widget.set_marker(28.54805,77.21872,command=stopclick, text="Asiad Village", font=('Courier New',9), marker_color_circle='white', marker_color_outside='green', text_color='black')
gul=map_widget.set_marker(28.55373,77.21222,command=stopclick, text="Gulmohar Park", font=('Courier New',9), marker_color_circle='white', marker_color_outside='green', text_color='black')
nee=map_widget.set_marker(28.55797,77.21777,command=stopclick, text="Neeti Bagh", font=('Courier New',9), marker_color_circle='white', marker_color_outside='green', text_color='black')
ayu=map_widget.set_marker(28.56109,77.22202,command=stopclick, text="Ayurvigyan Nagar", font=('Courier New',9), marker_color_circle='white', marker_color_outside='green', text_color='black')
shi=map_widget.set_marker(28.56645,77.22502,command=stopclick, text="Shiv Mandir", font=('Courier New',9), marker_color_circle='white', marker_color_outside='green', text_color='black')
pv5= map_widget.set_path([sch.position,sksii.position,ski.position,hk1.position,asi.position,gul.position,nee.position,ayu.position,shi.position,spv.position])
#pv9
kalka=map_widget.set_marker(28.52941,77.25234,command=stopclick, text="DDA Flats Kalkaji", font=('Courier New',9), marker_color_circle='white', marker_color_outside='gray', text_color='black')
manda=map_widget.set_marker(28.53295,77.25315,command=stopclick, text="Mandakini Enclave", font=('Courier New',9), marker_color_circle='white', marker_color_outside='gray', text_color='black')
shivap=map_widget.set_marker(28.53353,77.25449,command=stopclick, text="Shivalik Apartments", font=('Courier New',9), marker_color_circle='white', marker_color_outside='gray', text_color='black')
crmark2=map_widget.set_marker(28.53613,77.2535,command=stopclick, text="C.R. Park Market No. 2", font=('Courier New',9), marker_color_circle='white', marker_color_outside='gray', text_color='black')
mela=map_widget.set_marker(28.53799,77.25221,command=stopclick, text="Mela Ground", font=('Courier New',9), marker_color_circle='white', marker_color_outside='gray', text_color='black')
crmark1=map_widget.set_marker(28.53998,77.24855,command=stopclick, text="C.R. Park Market No. 1", font=('Courier New',9), marker_color_circle='white', marker_color_outside='gray', text_color='black')
crk=map_widget.set_marker(28.54026, 77.24373,command=stopclick, text="C.R. Park K Block", font=('Courier New',9), marker_color_circle='white', marker_color_outside='gray', text_color='black')
cra=map_widget.set_marker(28.543,77.24239,command=stopclick, text="C.R. Park A Block", font=('Courier New',9), marker_color_circle='white', marker_color_outside='gray', text_color='black')
defence=map_widget.set_marker(28.57488,77.2385,command=stopclick, text="Defence Colony", font=('Courier New',9), marker_color_circle='white', marker_color_outside='gray', text_color='black')
pv9= map_widget.set_path([kalka.position,manda.position,shivap.position,crmark2.position,mela.position,crmark1.position,crk.position,cra.position,defence.position,spv.position])
#pv20 UP
guj=map_widget.set_marker(28.64363,77.29127,command=stopclick, text="Gujarat Vihar", font=('Courier New',9), marker_color_circle='white', marker_color_outside='lime', text_color='black')
swasth=map_widget.set_marker(28.64038,77.28629,command=stopclick, text="Swasthya Vihar", font=('Courier New',9), marker_color_circle='white', marker_color_outside='lime', text_color='black')
walia=map_widget.set_marker(28.63283, 77.28072,command=stopclick, text="Walia Nursing Home", font=('Courier New',9), marker_color_circle='white', marker_color_outside='lime', text_color='black')
pv20up= map_widget.set_path([guj.position,swasth.position,walia.position,spv.position])

#FOR AVYAYA: for the down routes, you can plot em as the same, just set marker_color_circle='gray' to differentiate them

#------#

root.mainloop()
