#---imported libraries---#

from main2 import *
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
        userbox.insert(END, '#Admission Number')
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
    global pv1, pv2, pv3, pv4, pv5, pv6, pv7, pv8, pv9, pv10, pv11, pv12, pv13, pv14, pv15, pv16, pv17, pv18, pv19, pv20, pv21, pv22
    PV['text']=str(table.get())
    pv1.delete()
    pv2.delete()
    pv3.delete()
    pv4.delete()
    pv5.delete()
    pv6.delete()
    pv7.delete()
    pv8.delete()
    pv9.delete()
    pv10.delete()
    pv11.delete()
    pv12.delete()
    pv13.delete()
    pv14.delete()
    pv15.delete()
    pv16.delete()
    pv17.delete()
    pv18.delete()
    pv19.delete()
    pv20.delete()
    pv21.delete()
    pv22.delete()
    if str(table.get())[3::]=='1':
        pv1= map_widget.set_path([saketj.position,saketh.position,gyan.position,shivalik.position,malv1.position,sarv.position,swami.position,tito.position,sadiq.position,hudco.position,andrew.position,spv.position])
    elif str(table.get())[3::]=='2':
        pv2=map_widget.set_path([dda.position,jnu.position,ber.position,munmark.position,rkp.position,iit.position,saf.position,gp1.position,kid.position,jorb.position,spv.position])
    elif str(table.get())[3::]=='3':
        pv3= map_widget.set_path([cha.position,nmb.position,ae.position,jsm.position,saf2.position,lbn.position,ina.position,kid.position,sem.position,defe.position,spv.position])
    elif str(table.get())[3::]=='4':
        pv4= map_widget.set_path([jmi.position,ehi.position,zb.position,nfc.position,mb.position,se.position,spv.position])
    elif str(table.get())[3::]=='5':
        pv5=map_widget.set_path([sch.position,sksii.position,ski.position,hk1.position,asi.position,gul.position,nee.position,ayu.position,shi.position,spv.position])
    elif str(table.get())[3::]=='6':
        pv6=map_widget.set_path([sv.position,ek1.position,sn.position,ek2.position,ek3.position,ac.position,dc.position,tccm.position,spv.position])
    elif str(table.get())[3::]=='7':
        pv7=map_widget.set_path([kd.position,na.position,sn.position,kc.position,gkc.position,gkr.position,gks.position,gkn.position,guru.position,bir.position,bho.position,spv.position])
    elif str(table.get())[3::]=='8':
        pv8=map_widget.set_path([ke.position,ga.position,ya.position,nia.position,naa.position,gkiia.position,gkiib.position,pvh.position,spv.position])
    elif str(table.get())[3::]=='9':
        pv9= map_widget.set_path([kalka.position,manda.position,shivap.position,crmark2.position,mela.position,crmark1.position,crk.position,cra.position,defence.position,spv.position])
    elif str(table.get())[3::]=='10':
        pv10=map_widget.set_path([vv.position,vk.position,am.position,qm.position,mmtc.position,iit.position,gp1.position,aiims.position,spv.position])
    elif str(table.get())[3::]=='11':
        pv11=map_widget.set_path([sarita.position,jasola.position,nfc.position,ashram.position,bho.position,niz.position,spv.position])
    elif str(table.get())[3::]=='12':
        pv12=map_widget.set_path([maya.position,mans.position,kirti.position,shad.position,patel.position,raje.position,karol.position,rail.position,spv.position])
    elif str(table.get())[3::]=='13':
        pv13=map_widget.set_path([ashok.position,deraw.position,gujra.position,prat.position,shakti.position,kamlan.position,ramjas.position,jawa.position,malka.position,spv.position])
    elif str(table.get())[3::]=='14':
        pv14=map_widget.set_path([azadpur.position,mt3.position,mt2.position,tagore.position,parm.position,rev.position,drin.position,bana.position,khy.position,rajni.position,ludlo.position,civill.position,indra.position,kaka.position,ambed.position,spv.position])
    elif str(table.get())[3::]=='15':
        pv15=map_widget.set_path([rohini.position,uniq.position,gujrat.position,bank.position,kohat.position,panj.position,cinema.position,rohtak.position,video.position,gole.position,chowk.position,baroda.position,spv.position])
    elif str(table.get())[3::]=='16':
        pv16=map_widget.set_path([rssp.position,ms.position,pa.position,ashir.position,mithila.position,prince.position,him.position,agra.position,savfasc.position,ajanta.position,kunj.position,spv.position])
    elif str(table.get())[3::]=='17':
        pv17=map_widget.set_path([gtb.position,lick.position,surya.position,yojana.position,sreshtha.position,avc.position,je.position,kkd.position,pvhd.position,nv.position,lax.position,spv.position])
    elif str(table.get())[3::]=='18':
        pv18=map_widget.set_path([crpf.position,stand.position,vasun.position,dh.position,sama.position,aa.position,mvipi.position,sup.position,pol.position,manfas.position,mvipiv.position,spv.position])
    elif str(table.get())[3::]=='19':
        pv19=map_widget.set_path([gip.position,sfn.position,stt.position,rvn.position,jvv.position,mmh.position,nbv.position,sfn.position,dnb.position,cgv.position,spv.position])
    elif str(table.get())[3::]=='20':
        pv20= map_widget.set_path([guj.position,swasth.position,walia.position,spv.position])
    elif str(table.get())[3::]=='21':
        pv21=map_widget.set_path([chan.position,darya.position,nanak.position,azad.position,irwin.position,mandi.position,pand.position,spv.position])
    elif str(table.get())[3::]=='22':
        pv22=map_widget.set_path([edm.position,vidhi.position,silver.position,jai.position,ddam.position,para.position,tech.position,press.position,ekta.position,ankur.position,mdp.position,spv.position])
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
        #stopsbox['state']='normal'
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
#pv3
cha=map_widget.set_marker(28.58485,77.19265, command=stopclick,text="Chanakyapuri",font=('Courier New',9), marker_color_circle='white', marker_color_outside='blue', text_color='black')
nmb=map_widget.set_marker(28.57864,77.17594, command=stopclick,text="New Moti Bagh",font=('Courier New',9), marker_color_circle='white', marker_color_outside='blue', text_color='black')
ae=map_widget.set_marker(28.57328,77.17908, command=stopclick,text="Aradhana Enclave",font=('Courier New',9), marker_color_circle='white', marker_color_outside='blue', text_color='black')
jsm=map_widget.set_marker(28.56548,77.19669, command=stopclick,text="Chaudhary Jhandu Singh Marg",font=('Courier New',9), marker_color_circle='white', marker_color_outside='blue', text_color='black')
saf2=map_widget.set_marker(28.56533,77.20017, command=stopclick,text="Safdarjung Enclave II",font=('Courier New',9), marker_color_circle='white', marker_color_outside='blue', text_color='black')
lbn=map_widget.set_marker(28.5794,77.20809, command=stopclick,text="Lakshmi Bai Nagar",font=('Courier New',9), marker_color_circle='white', marker_color_outside='blue', text_color='black')
ina=map_widget.set_marker(28.57752,77.21055, command=stopclick,text="INA Colony",font=('Courier New',9), marker_color_circle='white', marker_color_outside='blue', text_color='black')
sem=map_widget.set_marker(28.56877,77.22041, command=stopclick,text="South Extension Market",font=('Courier New',9), marker_color_circle='white', marker_color_outside='blue', text_color='black')
defe=map_widget.set_marker(28.57619,77.22948, command=stopclick,text="Defence Colony 1",font=('Courier New',9), marker_color_circle='white', marker_color_outside='blue', text_color='black')
pv3= map_widget.set_path([cha.position,nmb.position,ae.position,jsm.position,saf2.position,lbn.position,ina.position,kid.position,sem.position,defe.position,spv.position])
#pv4
jmi=map_widget.set_marker(28.56101,77.2807, command=stopclick,text="Jamia Milia Islamia",font=('Courier New',9), marker_color_circle='white', marker_color_outside='light blue', text_color='black')
ehi=map_widget.set_marker(28.56131,77.2727, command=stopclick,text="Escorts Heart Institute",font=('Courier New',9), marker_color_circle='white', marker_color_outside='light blue', text_color='black')
zb=map_widget.set_marker(28.5622,77.27221, command=stopclick,text="Zakir Bagh",font=('Courier New',9), marker_color_circle='white', marker_color_outside='light blue', text_color='black')
nfc=map_widget.set_marker(28.56896,77.27577, command=stopclick,text="New Friends Colony",font=('Courier New',9), marker_color_circle='white', marker_color_outside='light blue', text_color='black')
mb=map_widget.set_marker(28.57264,77.26584, command=stopclick,text="Maharani Bagh",font=('Courier New',9), marker_color_circle='white', marker_color_outside='light blue', text_color='black')
se=map_widget.set_marker(28.58161,77.26582, command=stopclick,text="Siddharth Extension",font=('Courier New',9), marker_color_circle='white', marker_color_outside='light blue', text_color='black')
pv4= map_widget.set_path([jmi.position,ehi.position,zb.position,nfc.position,mb.position,se.position,spv.position])
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
#pv6
sv=map_widget.set_marker(28.55645,77.27768,command=stopclick, text="Sukhdev Vihar", font=('Courier New',9), marker_color_circle='white', marker_color_outside='white', text_color='black')
ek1=map_widget.set_marker(28.56074,77.26084,command=stopclick, text="East of Kailash C Block", font=('Courier New',9), marker_color_circle='white', marker_color_outside='white', text_color='black')
sn=map_widget.set_marker(28.556,77.25187,command=stopclick, text="Sant Nagar", font=('Courier New',9), marker_color_circle='white', marker_color_outside='white', text_color='black')
ek2=map_widget.set_marker(28.5583,77.24671,command=stopclick, text="East of Kailash D Block", font=('Courier New',9), marker_color_circle='white', marker_color_outside='white', text_color='black')
ek3=map_widget.set_marker(28.56031,77.24591,command=stopclick, text="East of Kailash E Block", font=('Courier New',9), marker_color_circle='white', marker_color_outside='white', text_color='black')
ac=map_widget.set_marker(28.56107, 77.24901,command=stopclick, text="Amar Colony", font=('Courier New',9), marker_color_circle='white', marker_color_outside='white', text_color='black')
dc=map_widget.set_marker(28.56222, 77.25019,command=stopclick, text="Dayanand Colony", font=('Courier New',9), marker_color_circle='white', marker_color_outside='white', text_color='black')
tccm=map_widget.set_marker(28.56857,77.24124,command=stopclick, text="3Cs Central Market", font=('Courier New',9), marker_color_circle='white', marker_color_outside='white', text_color='black')
pv6= map_widget.set_path([sv.position,ek1.position,sn.position,ek2.position,ek3.position,ac.position,dc.position,tccm.position,spv.position])
#pv7
kd=map_widget.set_marker(28.53944,77.26619,command=stopclick, text="Kalkaji Depot", font=('Courier New',9), marker_color_circle='white', marker_color_outside='dark green', text_color='black')
na=map_widget.set_marker(28.54552,77.25035,command=stopclick, text="Nehru Apartments", font=('Courier New',9), marker_color_circle='white', marker_color_outside='dark green', text_color='black')
kc=map_widget.set_marker(28.55461,77.24283,command=stopclick, text="Kailash Colony", font=('Courier New',9), marker_color_circle='white', marker_color_outside='dark green', text_color='black')
gkc=map_widget.set_marker(28.55086,77.23877,command=stopclick, text="Greater Kailash I C Block", font=('Courier New',9), marker_color_circle='white', marker_color_outside='dark green', text_color='black')
gkr=map_widget.set_marker(28.55149, 77.2374,command=stopclick, text="Greater Kailash I R Block", font=('Courier New',9), marker_color_circle='white', marker_color_outside='dark green', text_color='black')
gks=map_widget.set_marker(28.55142, 77.23528,command=stopclick, text="Greater Kailash I S Block", font=('Courier New',9), marker_color_circle='white', marker_color_outside='dark green', text_color='black')
gkn=map_widget.set_marker(28.55726, 77.23208,command=stopclick, text="Greater Kailash I N Block", font=('Courier New',9), marker_color_circle='white', marker_color_outside='dark green', text_color='black')
guru=map_widget.set_marker(28.58239, 77.24164,command=stopclick, text="Gurudwara Jungpura Extension", font=('Courier New',9), marker_color_circle='white', marker_color_outside='dark green', text_color='black')
bir=map_widget.set_marker(28.58294, 77.24469,command=stopclick, text="Birbal Park", font=('Courier New',9), marker_color_circle='white', marker_color_outside='dark green', text_color='black')
bho=map_widget.set_marker(28.58553, 77.24898,command=stopclick, text="Bhogal Market", font=('Courier New',9), marker_color_circle='white', marker_color_outside='dark green', text_color='black')
pv7= map_widget.set_path([kd.position,na.position,sn.position,kc.position,gkc.position,gkr.position,gks.position,gkn.position,guru.position,bir.position,bho.position,spv.position])
#pv8
ke=map_widget.set_marker(28.52612, 77.25856,command=stopclick, text="Kalkaji Extension", font=('Courier New',9), marker_color_circle='white', marker_color_outside='pink', text_color='black')
ga=map_widget.set_marker(28.52617, 77.25271,command=stopclick, text="Gangotri Apartments", font=('Courier New',9), marker_color_circle='white', marker_color_outside='pink', text_color='black')
ya=map_widget.set_marker(28.5269, 77.25197,command=stopclick, text="Yamuna Apartments", font=('Courier New',9), marker_color_circle='white', marker_color_outside='pink', text_color='black')
nia=map_widget.set_marker(28.528, 77.25043,command=stopclick, text="Nilgiri Apartments", font=('Courier New',9), marker_color_circle='white', marker_color_outside='pink', text_color='black')
naa=map_widget.set_marker(28.52796, 77.2481,command=stopclick, text="Narmada Apartments", font=('Courier New',9), marker_color_circle='white', marker_color_outside='pink', text_color='black')
gkiia=map_widget.set_marker(28.53059, 77.24709,command=stopclick, text="Greater Kailash II S Block", font=('Courier New',9), marker_color_circle='white', marker_color_outside='pink', text_color='black')
gkiib=map_widget.set_marker(28.53937, 77.24247,command=stopclick, text="Greater Kailash II E Block", font=('Courier New',9), marker_color_circle='white', marker_color_outside='pink', text_color='black')
pvh=map_widget.set_marker(28.5847, 77.2409,command=stopclick, text="Pragati Vihar Hostel", font=('Courier New',9), marker_color_circle='white', marker_color_outside='pink', text_color='black')
pv8= map_widget.set_path([ke.position,ga.position,ya.position,nia.position,naa.position,gkiia.position,gkiib.position,pvh.position,spv.position])
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
#pv10
vv=map_widget.set_marker(28.55891, 77.17053,command=stopclick, text="Vasant Vihar", font=('Courier New',9), marker_color_circle='white', marker_color_outside='brown', text_color='black')
vk=map_widget.set_marker(28.53441, 77.15224,command=stopclick, text="Vasant Kunj", font=('Courier New',9), marker_color_circle='white', marker_color_outside='brown', text_color='black')
am=map_widget.set_marker(28.50797, 77.17663,command=stopclick, text="Andheria Modh", font=('Courier New',9), marker_color_circle='white', marker_color_outside='brown', text_color='black')
qm=map_widget.set_marker(28.5244, 77.19011,command=stopclick, text="Qutub Minar", font=('Courier New',9), marker_color_circle='white', marker_color_outside='brown', text_color='black')
mmtc=map_widget.set_marker(28.5368, 77.19743,command=stopclick, text="MMTC DTC Bus Stop", font=('Courier New',9), marker_color_circle='white', marker_color_outside='brown', text_color='black')
aiims=map_widget.set_marker(28.56744, 77.20789,command=stopclick, text="AIIMS", font=('Courier New',9), marker_color_circle='white', marker_color_outside='brown', text_color='black')
pv10= map_widget.set_path([vv.position,vk.position,am.position,qm.position,mmtc.position,iit.position,gp1.position,aiims.position,spv.position])
#pv11
sarita=map_widget.set_marker(28.53139, 77.29436,command=stopclick, text="Sarita Vihar", font=('Courier New',9), marker_color_circle='white', marker_color_outside='red', text_color='black')
jasola=map_widget.set_marker(28.5354, 77.28469,command=stopclick, text="Jasola Vihar", font=('Courier New',9), marker_color_circle='white', marker_color_outside='red', text_color='black')
ashram=map_widget.set_marker(28.57421, 77.25699,command=stopclick, text="Ashram", font=('Courier New',9), marker_color_circle='white', marker_color_outside='red', text_color='black')
niz=map_widget.set_marker(28.59317, 77.24317,command=stopclick, text="Nizamuddin", font=('Courier New',9), marker_color_circle='white', marker_color_outside='red', text_color='black')
pv11= map_widget.set_path([sarita.position,jasola.position,nfc.position,ashram.position,bho.position,niz.position,spv.position])
#pv12
maya=map_widget.set_marker(28.63748, 77.13002,command=stopclick, text="Mayapuri Chowk", font=('Courier New',9), marker_color_circle='white', marker_color_outside='cyan', text_color='black')
mans=map_widget.set_marker(28.64088, 77.13542,command=stopclick, text="Mansarovar", font=('Courier New',9), marker_color_circle='white', marker_color_outside='cyan', text_color='black')
kirti=map_widget.set_marker(28.64963, 77.14356,command=stopclick, text="Kirti Nagar", font=('Courier New',9), marker_color_circle='white', marker_color_outside='cyan', text_color='black')
shad=map_widget.set_marker(28.65117, 77.15889,command=stopclick, text="Shadipur Metro Station", font=('Courier New',9), marker_color_circle='white', marker_color_outside='cyan', text_color='black')
patel=map_widget.set_marker(28.64935, 77.16202,command=stopclick, text="Patel Nagar", font=('Courier New',9), marker_color_circle='white', marker_color_outside='cyan', text_color='black')
raje=map_widget.set_marker(28.64236, 77.1778,command=stopclick, text="Rajendra Place Metro Station", font=('Courier New',9), marker_color_circle='white', marker_color_outside='cyan', text_color='black')
karol=map_widget.set_marker(28.64409, 77.18897,command=stopclick, text="Karol Bagh Metro Station", font=('Courier New',9), marker_color_circle='white', marker_color_outside='cyan', text_color='black')
rail=map_widget.set_marker(28.63535, 77.21534,command=stopclick, text="Railway Colony", font=('Courier New',9), marker_color_circle='white', marker_color_outside='cyan', text_color='black')
pv12= map_widget.set_path([maya.position,mans.position,kirti.position,shad.position,patel.position,raje.position,karol.position,rail.position,spv.position])
#pv13
ashok=map_widget.set_marker(28.69071, 77.17605,command=stopclick, text="Ashok Vihar", font=('Courier New',9), marker_color_circle='white', marker_color_outside='gold', text_color='black')
deraw=map_widget.set_marker(28.69959, 77.1904,command=stopclick, text="Derawal Nagar", font=('Courier New',9), marker_color_circle='white', marker_color_outside='gold', text_color='black')
gujra=map_widget.set_marker(28.69878, 77.1916,command=stopclick, text="Gujranwala Town", font=('Courier New',9), marker_color_circle='white', marker_color_outside='gold', text_color='black')
prat=map_widget.set_marker(28.68778, 77.19385,command=stopclick, text="Rana Pratap Bagh", font=('Courier New',9), marker_color_circle='white', marker_color_outside='gold', text_color='black')
shakti=map_widget.set_marker(28.68155, 77.19842,command=stopclick, text="Shakti Nagar", font=('Courier New',9), marker_color_circle='white', marker_color_outside='gold', text_color='black')
kamlan=map_widget.set_marker(28.68376, 77.20183,command=stopclick, text="Kamla Nagar", font=('Courier New',9), marker_color_circle='white', marker_color_outside='gold', text_color='black')
ramjas=map_widget.set_marker(28.68659, 77.20705,command=stopclick, text="Ramjas College", font=('Courier New',9), marker_color_circle='white', marker_color_outside='gold', text_color='black')
jawa=map_widget.set_marker(28.68103, 77.20878,command=stopclick, text="Jawahar Nagar", font=('Courier New',9), marker_color_circle='white', marker_color_outside='gold', text_color='black')
malka=map_widget.set_marker(28.67834, 77.20832,command=stopclick, text="Malka Ganj", font=('Courier New',9), marker_color_circle='white', marker_color_outside='gold', text_color='black')
pv13= map_widget.set_path([ashok.position,deraw.position,gujra.position,prat.position,shakti.position,kamlan.position,ramjas.position,jawa.position,malka.position,spv.position])
#pv14
azadpur=map_widget.set_marker(28.71051, 77.18581,command=stopclick, text="Azadpur", font=('Courier New',9), marker_color_circle='white', marker_color_outside='silver', text_color='black')
mt3=map_widget.set_marker(28.70982, 77.18802,command=stopclick, text="Model Town III", font=('Courier New',9), marker_color_circle='white', marker_color_outside='silver', text_color='black')
mt2=map_widget.set_marker(28.70954, 77.18902,command=stopclick, text="Model Town II", font=('Courier New',9), marker_color_circle='white', marker_color_outside='silver', text_color='black')
tagore=map_widget.set_marker(28.70522, 77.19963,command=stopclick, text="Tagore Park", font=('Courier New',9), marker_color_circle='white', marker_color_outside='silver', text_color='black')
parm=map_widget.set_marker(28.71029, 77.20661,command=stopclick, text="Parmanand Dusshera Ground", font=('Courier New',9), marker_color_circle='white', marker_color_outside='silver', text_color='black')
rev=map_widget.set_marker(28.69561, 77.21327,command=stopclick, text="Riviera Apartments", font=('Courier New',9), marker_color_circle='white', marker_color_outside='silver', text_color='black')
drin=map_widget.set_marker(28.69593, 77.21611,command=stopclick, text="DRDO", font=('Courier New',9), marker_color_circle='white', marker_color_outside='silver', text_color='black')
bana=map_widget.set_marker(28.69638, 77.2192,command=stopclick, text="Banarasi Das Estate", font=('Courier New',9), marker_color_circle='white', marker_color_outside='silver', text_color='black')
khy=map_widget.set_marker(28.69008, 77.22128,command=stopclick, text="Khyber Pass DTC Bus Stop", font=('Courier New',9), marker_color_circle='white', marker_color_outside='silver', text_color='black')
rajni=map_widget.set_marker(28.67282, 77.221,command=stopclick, text="Raj Niwas Marg", font=('Courier New',9), marker_color_circle='white', marker_color_outside='silver', text_color='black')
ludlo=map_widget.set_marker(28.67282, 77.22254,command=stopclick, text="Ludlo Castle", font=('Courier New',9), marker_color_circle='white', marker_color_outside='silver', text_color='black')
civill=map_widget.set_marker(28.68173, 77.22259,command=stopclick, text="Civil Lines", font=('Courier New',9), marker_color_circle='white', marker_color_outside='silver', text_color='black')
indra=map_widget.set_marker(28.68226, 77.22469,command=stopclick, text="Indraprastha College", font=('Courier New',9), marker_color_circle='white', marker_color_outside='silver', text_color='black')
kaka=map_widget.set_marker(28.60514, 77.23607,command=stopclick, text="Kaka Nagar", font=('Courier New',9), marker_color_circle='white', marker_color_outside='silver', text_color='black')
ambed=map_widget.set_marker(28.60236, 77.23149,command=stopclick, text="Ambedkar Nagar", font=('Courier New',9), marker_color_circle='white', marker_color_outside='silver', text_color='black')
pv14= map_widget.set_path([azadpur.position,mt3.position,mt2.position,tagore.position,parm.position,rev.position,drin.position,bana.position,khy.position,rajni.position,ludlo.position,civill.position,indra.position,kaka.position,ambed.position,spv.position])
#pv15
rohini=map_widget.set_marker(28.74055, 77.11897,command=stopclick, text="Rohini Sector 16", font=('Courier New',9), marker_color_circle='white', marker_color_outside='lavender', text_color='black')
uniq=map_widget.set_marker(28.71553, 77.13094,command=stopclick, text="Unique Apartments", font=('Courier New',9), marker_color_circle='white', marker_color_outside='lavender', text_color='black')
gujrat=map_widget.set_marker(28.69171, 77.11144,command=stopclick, text="Gujrat Apartments", font=('Courier New',9), marker_color_circle='white', marker_color_outside='lavender', text_color='black')
bank=map_widget.set_marker(28.69294, 77.1206,command=stopclick, text="Bank Vihar Apartments", font=('Courier New',9), marker_color_circle='white', marker_color_outside='lavender', text_color='black')
kohat=map_widget.set_marker(28.69737, 77.14203,command=stopclick, text="Kohat Enclave Metro Station", font=('Courier New',9), marker_color_circle='white', marker_color_outside='lavender', text_color='black')
panj=map_widget.set_marker(28.67291, 77.14588,command=stopclick, text="Punjabi Bagh Metro Station", font=('Courier New',9), marker_color_circle='white', marker_color_outside='lavender', text_color='black')
cinema=map_widget.set_marker(28.65954, 77.18992,command=stopclick, text="Liberty Cinema Hall", font=('Courier New',9), marker_color_circle='white', marker_color_outside='lavender', text_color='black')
rohtak=map_widget.set_marker(28.65787, 77.1941,command=stopclick, text="New Rohtak Road", font=('Courier New',9), marker_color_circle='white', marker_color_outside='lavender', text_color='black')
video=map_widget.set_marker(28.64481, 77.20423,command=stopclick, text="Videocon Tower", font=('Courier New',9), marker_color_circle='white', marker_color_outside='lavender', text_color='black')
gole=map_widget.set_marker(28.6339, 77.20546,command=stopclick, text="Gole Market", font=('Courier New',9), marker_color_circle='white', marker_color_outside='lavender', text_color='black')
chowk=map_widget.set_marker(28.62346, 77.21271,command=stopclick, text="Patel Chowk Metro Station", font=('Courier New',9), marker_color_circle='white', marker_color_outside='lavender', text_color='black')
baroda=map_widget.set_marker(28.61606, 77.23077,command=stopclick, text="Baroda House", font=('Courier New',9), marker_color_circle='white', marker_color_outside='lavender', text_color='black')
pv15= map_widget.set_path([rohini.position,uniq.position,gujrat.position,bank.position,kohat.position,panj.position,cinema.position,rohtak.position,video.position,gole.position,chowk.position,baroda.position,spv.position])
#pv16
rssp=map_widget.set_marker(28.62064, 77.30742,command=stopclick, text="Radha Swami Satsang Park", font=('Courier New',9), marker_color_circle='white', marker_color_outside='teal', text_color='black')
ms=map_widget.set_marker(28.61979, 77.30491,command=stopclick, text="Mayur Vihar II Metro Station", font=('Courier New',9), marker_color_circle='white', marker_color_outside='teal', text_color='black')
pa=map_widget.set_marker(28.61984, 77.3004,command=stopclick, text="Mayur Vihar Pocket A", font=('Courier New',9), marker_color_circle='white', marker_color_outside='teal', text_color='black')
ashir=map_widget.set_marker(28.6345, 77.30154,command=stopclick, text="Ashirwaad Apartments", font=('Courier New',9), marker_color_circle='white', marker_color_outside='teal', text_color='black')
mithila=map_widget.set_marker(28.63315, 77.2993,command=stopclick, text="Mithila Apartments", font=('Courier New',9), marker_color_circle='white', marker_color_outside='teal', text_color='black')
prince=map_widget.set_marker(28.63064, 77.29949,command=stopclick, text="Prince Apartments", font=('Courier New',9), marker_color_circle='white', marker_color_outside='teal', text_color='black')
him=map_widget.set_marker(28.63262, 77.30557,command=stopclick, text="Himalaya Apartments", font=('Courier New',9), marker_color_circle='white', marker_color_outside='teal', text_color='black')
agra=map_widget.set_marker(28.6297, 77.30806,command=stopclick, text="Agrasen Apartments", font=('Courier New',9), marker_color_circle='white', marker_color_outside='teal', text_color='black')
savfasc=map_widget.set_marker(28.62774, 77.30695,command=stopclick, text="Savarkar Apartments", font=('Courier New',9), marker_color_circle='white', marker_color_outside='teal', text_color='black')
ajanta=map_widget.set_marker(28.62805, 77.30792,command=stopclick, text="Ajanta Apartments", font=('Courier New',9), marker_color_circle='white', marker_color_outside='teal', text_color='black')
kunj=map_widget.set_marker(28.62214, 77.30091,command=stopclick, text="Saraswati Kunj", font=('Courier New',9), marker_color_circle='white', marker_color_outside='teal', text_color='black')
pv16= map_widget.set_path([rssp.position,ms.position,pa.position,ashir.position,mithila.position,prince.position,him.position,agra.position,savfasc.position,ajanta.position,kunj.position,spv.position])
#pv17
gtb=map_widget.set_marker(28.68658, 77.33111,command=stopclick, text="GTB Hospital", font=('Courier New',9), marker_color_circle='white', marker_color_outside='magenta', text_color='black')
lick=map_widget.set_marker(28.66429, 77.32058,command=stopclick, text="LIC Office", font=('Courier New',9), marker_color_circle='white', marker_color_outside='magenta', text_color='black')
surya=map_widget.set_marker(28.66953, 77.33174,command=stopclick, text="Surya Nagar", font=('Courier New',9), marker_color_circle='white', marker_color_outside='magenta', text_color='black')
yojana=map_widget.set_marker(28.66512, 77.31639,command=stopclick, text="Yojana Vihar", font=('Courier New',9), marker_color_circle='white', marker_color_outside='magenta', text_color='black')
sreshtha=map_widget.set_marker(28.66561, 77.31356,command=stopclick, text="Sreshtha Vihar", font=('Courier New',9), marker_color_circle='white', marker_color_outside='magenta', text_color='black')
avc=map_widget.set_marker(28.64942, 77.30079,command=stopclick, text="Anand Vihar Colony", font=('Courier New',9), marker_color_circle='white', marker_color_outside='magenta', text_color='black')
je=map_widget.set_marker(28.64737, 77.30266,command=stopclick, text="Jagriti Enclave", font=('Courier New',9), marker_color_circle='white', marker_color_outside='magenta', text_color='black')
kkd=map_widget.set_marker(28.64655, 77.30156,command=stopclick, text="Karkardooma", font=('Courier New',9), marker_color_circle='white', marker_color_outside='magenta', text_color='black')
pvhd=map_widget.set_marker(28.63921, 77.29178,command=stopclick, text="Preet Vihar", font=('Courier New',9), marker_color_circle='white', marker_color_outside='magenta', text_color='black')
nv=map_widget.set_marker(28.63608, 77.2859,command=stopclick, text="Nirman Vihar", font=('Courier New',9), marker_color_circle='white', marker_color_outside='magenta', text_color='black')
lax=map_widget.set_marker(28.62963, 77.27606,command=stopclick, text="Laxmi Nagar", font=('Courier New',9), marker_color_circle='white', marker_color_outside='magenta', text_color='black')
pv17= map_widget.set_path([gtb.position,lick.position,surya.position,yojana.position,sreshtha.position,avc.position,je.position,kkd.position,pvhd.position,nv.position,lax.position,spv.position])
#pv18
crpf=map_widget.set_marker(28.60798, 77.33958,command=stopclick, text="CRPF Camp", font=('Courier New',9), marker_color_circle='white', marker_color_outside='violet', text_color='black')
stand=map_widget.set_marker(28.60756, 77.33641,command=stopclick, text="St. Andrews Public School", font=('Courier New',9), marker_color_circle='white', marker_color_outside='violet', text_color='black')
vasun=map_widget.set_marker(28.60016, 77.31649,command=stopclick, text="Vasundhara Enclave", font=('Courier New',9), marker_color_circle='white', marker_color_outside='violet', text_color='black')
dh=map_widget.set_marker(28.6026, 77.31306,command=stopclick, text="Dharamshila Hospital", font=('Courier New',9), marker_color_circle='white', marker_color_outside='violet', text_color='black')
sama=map_widget.set_marker(28.59627, 77.29519,command=stopclick, text="Samachar Apartments", font=('Courier New',9), marker_color_circle='white', marker_color_outside='violet', text_color='black')
aa=map_widget.set_marker(28.59851, 77.29763,command=stopclick, text="Ashiana Apartments", font=('Courier New',9), marker_color_circle='white', marker_color_outside='violet', text_color='black')
mvipi=map_widget.set_marker(28.60689, 77.29472,command=stopclick, text="Mayur Vihar I Pocket I", font=('Courier New',9), marker_color_circle='white', marker_color_outside='violet', text_color='black')
sup=map_widget.set_marker(28.60759, 77.2916,command=stopclick, text="Supreme Enclave", font=('Courier New',9), marker_color_circle='white', marker_color_outside='violet', text_color='black')
pol=map_widget.set_marker(28.61146, 77.28722,command=stopclick, text="Police Apartments", font=('Courier New',9), marker_color_circle='white', marker_color_outside='violet', text_color='black')
manfas=map_widget.set_marker(28.61098, 77.28639,command=stopclick, text="Manu Apartments", font=('Courier New',9), marker_color_circle='white', marker_color_outside='violet', text_color='black')
mvipiv=map_widget.set_marker(28.61083, 77.28481,command=stopclick, text="Mayur Vihar I Pocket IV Metro Station", font=('Courier New',9), marker_color_circle='white', marker_color_outside='violet', text_color='black')
pv18= map_widget.set_path([crpf.position,stand.position,vasun.position,dh.position,sama.position,aa.position,mvipi.position,sup.position,pol.position,manfas.position,mvipiv.position,spv.position])
#pv19
gip=map_widget.set_marker(28.56919, 77.32799,command=stopclick, text="GIP Mall", font=('Courier New',9), marker_color_circle='white', marker_color_outside='dark blue', text_color='black')
sfn=map_widget.set_marker(28.5619, 77.33881,command=stopclick, text="Sector 44 Noida", font=('Courier New',9), marker_color_circle='white', marker_color_outside='dark blue', text_color='black')
stt=map_widget.set_marker(28.5672, 77.34596,command=stopclick, text="Sector 32 Golf Course Metro Station", font=('Courier New',9), marker_color_circle='white', marker_color_outside='dark blue', text_color='black')
rvn=map_widget.set_marker(28.57584, 77.33986,command=stopclick, text="Ram Vihar", font=('Courier New',9), marker_color_circle='white', marker_color_outside='dark blue', text_color='black')
jvv=map_widget.set_marker(28.58382, 77.33555,command=stopclick, text="Jalvayu Vihar", font=('Courier New',9), marker_color_circle='white', marker_color_outside='dark blue', text_color='black')
mmh=map_widget.set_marker(28.57947, 77.32117,command=stopclick, text="Max Medicare Hospital", font=('Courier New',9), marker_color_circle='white', marker_color_outside='dark blue', text_color='black')
nbv=map_widget.set_marker(28.58188, 77.31409,command=stopclick, text="Naya Bans Village", font=('Courier New',9), marker_color_circle='white', marker_color_outside='dark blue', text_color='black')
sfn=map_widget.set_marker(28.58248, 77.3044,command=stopclick, text="Sector 14A Noida", font=('Courier New',9), marker_color_circle='white', marker_color_outside='dark blue', text_color='black')
dnb=map_widget.set_marker(28.58211, 77.30263,command=stopclick, text="Delhi Noida Border", font=('Courier New',9), marker_color_circle='white', marker_color_outside='dark blue', text_color='black')
cgv=map_widget.set_marker(28.61028, 77.27267,command=stopclick, text="Commonwealth Games Village", font=('Courier New',9), marker_color_circle='white', marker_color_outside='dark blue', text_color='black')
pv19= map_widget.set_path([gip.position,sfn.position,stt.position,rvn.position,jvv.position,mmh.position,nbv.position,sfn.position,dnb.position,cgv.position,spv.position])
#pv20
guj=map_widget.set_marker(28.64363,77.29127,command=stopclick, text="Gujarat Vihar", font=('Courier New',9), marker_color_circle='white', marker_color_outside='lime', text_color='black')
swasth=map_widget.set_marker(28.64038,77.28629,command=stopclick, text="Swasthya Vihar", font=('Courier New',9), marker_color_circle='white', marker_color_outside='lime', text_color='black')
walia=map_widget.set_marker(28.63283, 77.28072,command=stopclick, text="Walia Nursing Home", font=('Courier New',9), marker_color_circle='white', marker_color_outside='lime', text_color='black')
pv20= map_widget.set_path([guj.position,swasth.position,walia.position,spv.position])
#pv21
chan=map_widget.set_marker(28.65325, 77.23652,command=stopclick, text="Chandni Chowk", font=('Courier New',9), marker_color_circle='white', marker_color_outside='yellow', text_color='black')
darya=map_widget.set_marker(28.64481, 77.24032,command=stopclick, text="Darya Ganj", font=('Courier New',9), marker_color_circle='white', marker_color_outside='yellow', text_color='black')
nanak=map_widget.set_marker(28.63807, 77.23113,command=stopclick, text="Guru Nanak Eye Center", font=('Courier New',9), marker_color_circle='white', marker_color_outside='yellow', text_color='black')
azad=map_widget.set_marker(28.63592, 77.24013,command=stopclick, text="Maulana Azad Medical College", font=('Courier New',9), marker_color_circle='white', marker_color_outside='yellow', text_color='black')
irwin=map_widget.set_marker(28.62553, 77.23644,command=stopclick, text="Lady Irwin College", font=('Courier New',9), marker_color_circle='white', marker_color_outside='yellow', text_color='black')
mandi=map_widget.set_marker(28.62561, 77.23426,command=stopclick, text="Mandi House Metro Station", font=('Courier New',9), marker_color_circle='white', marker_color_outside='yellow', text_color='black')
pand=map_widget.set_marker(28.60597, 77.23071,command=stopclick, text="Pandara Road", font=('Courier New',9), marker_color_circle='white', marker_color_outside='yellow', text_color='black')
pv21= map_widget.set_path([chan.position,darya.position,nanak.position,azad.position,irwin.position,mandi.position,pand.position,spv.position])
#pv22
edm=map_widget.set_marker(28.64213, 77.31627,command=stopclick, text="EDM Mall", font=('Courier New',9), marker_color_circle='white', marker_color_outside='black', text_color='black')
vidhi=map_widget.set_marker(28.63333, 77.31026,command=stopclick, text="Vidhi Apartments", font=('Courier New',9), marker_color_circle='white', marker_color_outside='black', text_color='black')
silver=map_widget.set_marker(28.63632, 77.31222,command=stopclick, text="Silver Oak Apartments", font=('Courier New',9), marker_color_circle='white', marker_color_outside='black', text_color='black')
jai=map_widget.set_marker(28.63046, 77.31053,command=stopclick, text="Jai Apartments", font=('Courier New',9), marker_color_circle='white', marker_color_outside='black', text_color='black')
ddam=map_widget.set_marker(28.62981, 77.30852,command=stopclick, text="DDA Market", font=('Courier New',9), marker_color_circle='white', marker_color_outside='black', text_color='black')
para=map_widget.set_marker(28.62621, 77.30821,command=stopclick, text="Paradise Apartments", font=('Courier New',9), marker_color_circle='white', marker_color_outside='black', text_color='black')
tech=map_widget.set_marker(28.62449, 77.30294,command=stopclick, text="Technology Apartments", font=('Courier New',9), marker_color_circle='white', marker_color_outside='black', text_color='black')
press=map_widget.set_marker(28.62304, 77.29858,command=stopclick, text="Press Apartments", font=('Courier New',9), marker_color_circle='white', marker_color_outside='black', text_color='black')
ekta=map_widget.set_marker(28.62129, 77.29332,command=stopclick, text="Ekta Gardens", font=('Courier New',9), marker_color_circle='white', marker_color_outside='black', text_color='black')
ankur=map_widget.set_marker(28.62015, 77.29016,command=stopclick, text="Ankur Apartments", font=('Courier New',9), marker_color_circle='white', marker_color_outside='black', text_color='black')
mdp=map_widget.set_marker(28.61861, 77.28664,command=stopclick, text="Mother Dairy Patparganj", font=('Courier New',9), marker_color_circle='white', marker_color_outside='black', text_color='black')
pv22= map_widget.set_path([edm.position,vidhi.position,silver.position,jai.position,ddam.position,para.position,tech.position,press.position,ekta.position,ankur.position,mdp.position,spv.position])

#FOR AVYAYA: for the down routes, you can plot em as the same, just set marker_color_circle='gray' to differentiate them

#------#

root.mainloop()
