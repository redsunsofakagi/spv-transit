#importing modules
import csv
import bcrypt
import mysql.connector as sqlcon

#connecting to mysql
conn = sqlcon.connect(host = "localhost", user = "root", passwd = "1234", database = "spv_transit")
cur=conn.cursor()

#cheking connection
if conn.is_connected():
    print("Mysql connector is connected")
else:
    print("Connection failed")

#funtion to create a new account
def create_account(username, permissions, password):
    salt=bcrypt.gensalt()
    potato=bytes(password, 'utf-8')
    hash_brown=bcrypt.hashpw(potato,salt)
    quer1="INSERT INTO logins (username, permission, password_hash, salt) VALUES ('{}','{}','{}','{}')".format(username, permissions, hash_brown.decode('ASCII'), salt.decode('ASCII'))
    try:
        cur.execute(quer1)
        conn.commit()
        print("account successfuly created")
        return True
    except (sqlcon.Error, sqlcon.Warning) as e:
        print(e)
        return False

#funtion to verify username and password and login and return boolean
def login(username, permissions, password):
    quer1="SELECT * FROM logins WHERE (username='{}' && permission='{}')".format(username, permissions)
    try:
        cur.execute(quer1)
    except (sqlcon.Error, sqlcon.Warning) as e:
        print(e)
        return None
    data=cur.fetchone()

    login_data={'name':data[0], 'type':data[1], 'passw':data[2], "salt":data[3]}
    hashed=bcrypt.hashpw(bytes(password,'utf-8'), bytes(login_data['salt'], 'utf-8'))

    if hashed.decode('ASCII') == login_data['passw']:
        return True
    else:
        return False


#function to return all data for a given route in the form of a dictionary
def route_fetch(n):
    if n<=22 and n>=1:
        quer1="SELECT * FROM bus_routes WHERE route_num='{}'".format(n,)
        quer2="SELECT * FROM drivers WHERE route_num='{}'".format(n,)
        quer3="SELECT * FROM attendants WHERE route_num='{}'".format(n,)
        try:
            cur.execute(quer1)
            route_data=cur.fetchone()
            cur.execute(quer2)
            driver_data=cur.fetchone()
            cur.execute(quer3)
            attendant_data=cur.fetchone()
        except (sqlcon.Error, sqlcon.Warning) as e:
            print("There is an error!")
            print(e)
            return None
    else:
        print("Enter a valid route number")
        return None
    
    route_dic={'route':route_data, 'driver':driver_data, 'attendant':attendant_data}
    return route_dic

#function to fetch all details for a given pass_id
def pass_fetch(pass_id):
    quer1="SELECT * FROM passengers WHERE pass_id='{}'".format(pass_id,)
    try:
        cur.execute(quer1)
        pass_data=cur.fetchall()
    except (sqlcon.Error, sqlcon.Warning) as e:
        print(e)
        return None
    
    pass_dic={'username':pass_data[0][0], 'name':pass_data[0][1], 'route':pass_data[0][2]}
    
    
#function to fetch all details for a given stop_id
def stop_fetch(stop_id):
    quer1="SELECT stop_name, route_num, latitude, longitiude, stop_address, pass_count, morning_time, evening_time FROM stops WHERE stop_id='{}'".format(stop_id,)
    try:
        cur.execute(quer1)
        stop_data=cur.fetchall()
    except:
        pass
    route_dic= {'stop_name':stop_data[0], 'route_num':stop_data[1], 'latitude':stop_data[2],
     'longitude':stop_data[3],'stop_address':stop_data[4], 'pass_count':stop_data[5],
     'morning_time':stop_data[6],'evening_time':[7]}
    return route_dic

#function to updata data if you are a student account

def pass_update(pass_id, pass_dic):
    quer1="SELECT pass_name, route_num, stop_id, pass_phnum from passengers WHERE pass_id='{}'".format(pass_id,)

    pass

#function to update data for a admin account
def admin_update():
    pass


#create_account('arin','attendant','1234')
print(login('arin', 'attendant','1234') )
#print(route_fetch(22))

conn.close()