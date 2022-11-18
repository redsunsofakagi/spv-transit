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

def logins_create(filename):
    with open(filename, "r", newline="") as fin:
        csvreader=csv.reader(fin)
        head=True
        for i in csvreader:
            if head==True:
                head=False
                continue
            create_account(i[0],"passenger",'1234')

            

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
        for i in csvreader:
            print(i)
            quer1="INSERT INTO passengers VALUES('{}','{}','{}','{}','{}')".format(i[0].strip(),i[1].strip(),int(i[2].strip()),i[3].strip(),i[4].strip())
            try:
                cur.execute(quer1)
                conn.commit()
            except(sqlcon.Error,sqlcon.Warning) as e:
                print(e)
                conn.rollback()

path="csv\\"
logins_create("passengers.csv")
bus_routes_create(path+"bus_routes.csv")
stops_create(path+"csv")
passengers_create(path+"passengers.csv")
drivers_create(path+"passengers.csv")
conductors_create(path+"conductors.csv")
attendants_create(path+"attendants.csv")