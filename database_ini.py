import csv
import mysql.connector as sqlcon
import sys
from backend import *

#connecting to mysql
conn = sqlcon.connect(host = "localhost", user = "root", passwd = "1234", database = "spv_transit")
cur=conn.cursor()

#cheking connection
if conn.is_connected():
    pass
else:
    print("Connection failed. Aborting.")
    sys.exit()


def tables_create():
    quer1="CREATE TABLE  IF NOT EXISTS logins (username varchar(20) UNIQUE,permission enum('attendant', 'passenger'),password_hash tinytext,salt tinytext) "
    quer2="CREATE TABLE IF NOT EXISTS bus_routes(route_num int NOT NULL PRIMARY KEY,route_length decimal(3,1),stop_count int,capacity int)"
    quer3="CREATE TABLE  IF NOT EXISTS stops(stop_id varchar(10) NOT NULL PRIMARY KEY,stop_name varchar(100),route_num int,latitude decimal(7,5),longitude decimal(7,5),pass_count int,morning_time time,FOREIGN KEY (route_num) REFERENCES bus_routes (route_num)ON DELETE CASCADE ON UPDATE CASCADE)"
    quer4="CREATE TABLE  IF NOT EXISTS passengers(pass_id varchar(20) UNIQUE NOT NULL ,pass_name varchar(50),route_num int,stop_id varchar(10) NOT NULL,pass_phnum char(10),    FOREIGN KEY (route_num) REFERENCES bus_routes (route_num)ON DELETE CASCADE ON UPDATE CASCADE,FOREIGN KEY (stop_id) REFERENCES stops (stop_id)ON DELETE CASCADE ON UPDATE CASCADE,FOREIGN KEY(pass_id) REFERENCES logins(username)ON DELETE CASCADE ON UPDATE CASCADE)"
    quer5="CREATE TABLE IF NOT EXISTS drivers (route_num int UNIQUE NOT NULL,driver_name varchar(50) NOT NULL,driver_phnum char(10),FOREIGN KEY (route_num) REFERENCES bus_routes (route_num)ON DELETE CASCADE ON UPDATE CASCADE)"
    quer6="CREATE TABLE IF NOT EXISTS conductors (route_num int UNIQUE NOT NULL,conductor_name varchar(50) NOT NULL,conductor_phnum char(10),FOREIGN KEY (route_num) REFERENCES bus_routes (route_num)ON DELETE CASCADE ON UPDATE CASCADE)"
    quer7="CREATE TABLE  IF NOT EXISTS attendants (route_num int UNIQUE NOT NULL,attendant_name varchar(50),attendant_phnum varchar(20) UNIQUE,FOREIGN KEY (route_num) REFERENCES bus_routes (route_num)ON DELETE CASCADE ON UPDATE CASCADE,FOREIGN KEY (attendant_phnum) REFERENCES logins (username)ON DELETE CASCADE ON UPDATE CASCADE)"
    try:
        cur.execute(quer1)
        cur.execute(quer2)
        cur.execute(quer3)
        cur.execute(quer4)
        cur.execute(quer5)
        cur.execute(quer6)
        cur.execute(quer7)
        conn.commit()               
    except(sqlcon.Error,sqlcon.Warning) as e:
        print(e)
        conn.rollback()


def tables_delete():
    quer1="DROP TABLE attendants"
    quer2="DROP TABLE conductors"
    quer3="DROP TABLE drivers"
    quer4="DROP TABLE passengers"
    quer5="DROP TABLE stops"
    quer6="DROP TABLE bus_routes"
    quer7="DROP TABLE logins"
    try:
        cur.execute(quer1)
        cur.execute(quer2)
        cur.execute(quer3)
        cur.execute(quer4)
        cur.execute(quer5)
        cur.execute(quer6)
        cur.execute(quer7)
        conn.commit()               
    except(sqlcon.Error,sqlcon.Warning) as e:
        print(e)
        conn.rollback()


def logins_create(filename1, filename2):
    with open(filename1, "r", newline="") as fin:
        csvreader=csv.reader(fin)
        head=True
        for i in csvreader:
            if head==True:
                head=False
                continue
            create_account(i[0],"passenger",'1234')
    with open(filename2, "r", newline="") as fin:
        csvreader=csv.reader(fin)
        head=True
        for i in csvreader:
            if head==True:
                head=False
                continue
            create_account(i[2],"attendant",'1234')
        

            

def bus_routes_create(filename):
    with open(filename, "r", newline="") as fin:
        csvreader=csv.reader(fin)
        head=True
        for i in csvreader:
            if head==True:
                head=False
                continue
            quer1="INSERT INTO bus_routes(route_num, route_length, stop_count, capacity) VALUES('{}',{},{},{})".format(int(i[0].strip()),i[1].strip(),i[2].strip(),i[3].strip())
            try:
                cur.execute(quer1)
                conn.commit()
            except(sqlcon.Error,sqlcon.Warning) as e:
                print(e)
                conn.rollback()


def stops_create(filename):
    with open(filename, "r", newline="") as fin:
        csvreader=csv.reader(fin)
        head=True
        for i in csvreader:
            #print(i)
            if head==True:
                head=False
                continue
            quer1="INSERT INTO stops VALUES('{}','{}','{}',{},{},{},'{}')".format(i[0].strip(),i[1].strip(),int(i[2].strip()),float(i[3].strip()),float(i[4].strip()),int(i[5].strip()),i[6].strip())
            #print(quer1)
            try:
                cur.execute(quer1)
                conn.commit()
                
            except(sqlcon.Error,sqlcon.Warning) as e:
                print(e)
                conn.rollback()


def drivers_create(filename):
    with open(filename, "r", newline="") as fin:
        csvreader=csv.reader(fin)
        head=True
        for i in csvreader:
            if head==True:
                head=False
                continue
            quer1="INSERT INTO drivers VALUES('{}','{}','{}')".format(int(i[0].strip()),i[1].strip(),i[2].strip())
            try:
                cur.execute(quer1)
                conn.commit()
            except(sqlcon.Error,sqlcon.Warning) as e:
                print(e)
                conn.rollback()


def conductors_create(filename):
    with open(filename, "r", newline="") as fin:
        csvreader=csv.reader(fin)
        head=True
        for i in csvreader:
            if head==True:
                head=False
                continue
            quer1="INSERT INTO conductors VALUES('{}','{}','{}')".format(int(i[0].strip()),i[1].strip(),i[2].strip())
            try:
                cur.execute(quer1)
                conn.commit()
            except(sqlcon.Error,sqlcon.Warning) as e:
                print(e)
                conn.rollback()


def attendants_create(filename):
    with open(filename, "r", newline="") as fin:
        csvreader=csv.reader(fin)
        head=True
        for i in csvreader:
            if head==True:
                head=False
                continue
            quer1="INSERT INTO attendants VALUES('{}','{}','{}')".format(int(i[0].strip()),i[1].strip(),i[2].strip())
            try:
                cur.execute(quer1)
                conn.commit()
            except(sqlcon.Error,sqlcon.Warning) as e:
                print(e)
                conn.rollback()


def passengers_create(filename):
    with open(filename, "r", newline="") as fin:
        csvreader=csv.reader(fin,delimiter=",")
        head=True
        for i in csvreader:
            if head==True:
                head=False
                continue
            print(i)
            quer1="INSERT INTO passengers VALUES('{}','{}','{}','{}','{}')".format(i[0].strip(),i[1].strip(),int(i[2].strip()),i[3].strip(),i[4].strip())
            try:
                cur.execute(quer1)
                conn.commit()
            except(sqlcon.Error,sqlcon.Warning) as e:
                print(e)
                conn.rollback()
path="csv/"
#path="csv\\"

tables_delete()
tables_create()
logins_create(path+"passengers.csv",path+"attendants.csv")
bus_routes_create(path+"bus_routes.csv")
stops_create(path+"stops.csv")
passengers_create(path+"passengers.csv")
drivers_create(path+"drivers.csv")
conductors_create(path+"conductors.csv")
attendants_create(path+"attendants.csv")