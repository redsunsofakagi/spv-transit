#importing modules
import sys
import bcrypt
import mysql.connector as sqlcon

#connecting to mysql
conn = sqlcon.connect(host = "localhost", user = "root", passwd = "1234", database = "spv_transit")
cur=conn.cursor()

#cheking connection
if conn.is_connected():
    pass
else:
    print("Connection failed. Aborting.")
    sys.exit()

#funtion to create a new account
def create_account(username, permissions, password):
    salt=bcrypt.gensalt()
    potato=bytes(password, 'utf-8')
    hash_brown=bcrypt.hashpw(potato,salt)
    quer1="INSERT INTO logins (username, permission, password_hash, salt) VALUES ('{}','{}','{}','{}')".format(username, permissions, hash_brown.decode('ASCII'), salt.decode('ASCII'))
    try:
        cur.execute(quer1)
        conn.commit()
        return True
    except (sqlcon.Error, sqlcon.Warning) as e:
        conn.rollback()
        print(e)
        return False

def update_account(username, permissions, password):
    salt=bcrypt.gensalt()
    potato=bytes(password, 'utf-8')
    hash_brown=bcrypt.hashpw(potato,salt)
    quer1="UPDATE logins SET permission='{}', password_hash='{}', salt='{}' WHERE username='{}'".format(permissions, hash_brown.decode('ASCII'), salt.decode('ASCII'),username)
    try:
        cur.execute(quer1)
        conn.commit()
        return True
    except (sqlcon.Error, sqlcon.Warning) as e:
        conn.rollback()
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
        quer1="SELECT * FROM bus_routes WHERE route_num={}".format(n,)
        quer2="SELECT * FROM drivers WHERE route_num={}".format(n,)
        quer3="SELECT * FROM attendants WHERE route_num={}".format(n,)
        quer4="SELECT * FROM conductors WHERE route_num={}".format(n,)
        try:
            cur.execute(quer1)
            route_data=cur.fetchone()
            cur.execute(quer2)
            driver_data=cur.fetchone()
            cur.execute(quer3)
            attendant_data=cur.fetchone()
            cur.execute(quer4)
            conductor_data=cur.fetchone()
        except (sqlcon.Error, sqlcon.Warning) as e:
            print("There is an error!")
            print(e)
            return None
    else:
        print("Enter a valid route number.")
        return None
    
    route_data_dic={'route_length':route_data[1],'stop_count':route_data[2], 'capacity':route_data[3]}
    driver_data_dic={'driver_name':driver_data[1], 'driver_phnum':driver_data[2]}
    attendant_data_dic={'attendant_name':attendant_data[1], 'attendant_phnum':attendant_data[2]}
    conductor_data_dic={'conductor_name':conductor_data[1], 'conductor_phnum':conductor_data[2]}

    route_dic={'route':route_data_dic, 'driver':driver_data_dic, 'attendant':attendant_data_dic, 'conductor':conductor_data_dic}
    return route_dic


#function to fetch all details for a given pass_id
def pass_fetch(pass_id):
    quer1="SELECT * FROM passengers WHERE pass_id='{}'".format(pass_id,)
    try:
        cur.execute(quer1)
        pass_data=cur.fetchone()
    except (sqlcon.Error, sqlcon.Warning) as e:
        print(e)
        return None

    pass_dic={'pass_id':pass_data[0], 'name':pass_data[1], 'route':pass_data[2], 'stop_id':pass_data[3], 'pass_phnum':pass_data[4]}
    return pass_dic
    
    
#function to fetch all details for a given stop_id
def stop_fetch(stop_id):
    quer1="SELECT * FROM stops WHERE stop_id='{}'".format(stop_id,)
    try:
        cur.execute(quer1)
        stop_data=cur.fetchone()
    except (sqlcon.Error, sqlcon.Warning) as e:
        print(e)
        return None

    route_dic= {'stop_name':stop_data[1], 'route_num':stop_data[2], 'latitude':stop_data[3],
     'longitude':stop_data[4], 'pass_count':stop_data[5],
     'morning_time':stop_data[6]}
    return route_dic



#function to updata data if you are a passenger account

def pass_update(pass_id, pass_name, route_num, stop_id, pass_phnum):
    quer1="SELECT * FROM passengers WHERE pass_id='{}'".format(pass_id,)
    try:
        cur.execute(quer1)
        pass_data=cur.fetchone()
    except (sqlcon.Error, sqlcon.Warning) as e:
        print(e)
    lst=[pass_id, pass_name, route_num, stop_id, pass_phnum]
    for i in range (len(lst)):
        if lst[i]==None:
            lst[i]=pass_data[i]

    quer2="UPDATE passengers SET pass_name='{}', route_num={}, stop_id='{}', pass_phnum='{}' WHERE pass_id='{}'".format(lst[1], lst[2], lst[3], lst[4], lst[0])
    try:
        cur.execute(quer2)
        conn.commit()
    except (sqlcon.Error, sqlcon.Warning) as e:
        conn.rollback()
        print(e)
    
# this function is too long but I am not recoding it
#function to update data for a admin account
#Enter None where there is no change
# Content_list format: [[length_route, capacity], [attendant_name], [driver_name, contact], [conductor_name, contact],[stop_id, number of passengers]]
def attendant_update(attendant_phnum, content_list ):
    quer1="SELECT route_num FROM attendants WHERE attendant_phnum={}".format(attendant_phnum,)
    try:
        cur.execute(quer1)
        route_num_data=cur.fetchone()
    except (sqlcon.Error, sqlcon.Warning) as e:
        print(e)
    route_num=route_num_data[0]
    quer2="SELECT route_length, capacity from bus_routes WHERE route_num={}".format(route_num,)
    quer3="SELECT attendant_name, attendant_phnum from attendants WHERE route_num={}".format(route_num,)
    quer4="SELECT driver_name, driver_phnum from drivers WHERE route_num={}".format(route_num,)
    quer5="SELECT conductor_name, conductor_phnum from conductors WHERE route_num={}".format(route_num,)
    quer6="SELECT pass_count from stops WHERE stop_id='{}'".format(content_list[4][0],)
    #print(content_list)
    try:
        cur.execute(quer2)
        route_data=cur.fetchone()
        cur.execute(quer3)
        attendant_data=cur.fetchone()
        cur.execute(quer4)
        driver_data=cur.fetchone()
        cur.execute(quer5)
        conductor_data=cur.fetchone()
        cur.execute(quer6)
        stop_data=cur.fetchone()
    except (sqlcon.Error, sqlcon.Warning) as e:
        print(e)
    #print(stop_data)
    old_content=[route_data, attendant_data, driver_data, conductor_data, stop_data]
    #print(content_list[4][0])
    for i in range(len(content_list)):
        for j in range (len(content_list[i])):
            if content_list[i][j]==None:
                content_list[i][j]=old_content[i][j]
    quer7="UPDATE bus_routes SET route_length={}, capacity={} WHERE route_num={}".format(content_list[0][0], content_list[0][1], route_num)
    quer8="UPDATE attendants SET attendant_name='{}' WHERE route_num={}".format(content_list[1][0], route_num)   
    quer9="UPDATE drivers SET driver_name='{}', driver_phnum='{}' WHERE route_num={}".format(content_list[2][0], content_list[2][1],route_num)
    quer10="UPDATE conductors SET conductor_name='{}', conductor_phnum='{}' WHERE route_num={}".format(content_list[3][0], content_list[3][1], route_num)
    quer11="UPDATE stops SET pass_count={} WHERE stop_id='{}'".format(content_list[4][1],content_list[4][0])

    try:
        cur.execute(quer7)
        cur.execute(quer8)
        cur.execute(quer9)
        cur.execute(quer10)
        cur.execute(quer11)
        conn.commit()
    except (sqlcon.Error, sqlcon.Warning) as e:
        conn.rollback()
        print(e)



#create_account(username, permissions, password)
#login(username, permissions, password)
#route_fetch(n)
#pass_fetch(pass_id)
#stop_fetch(stop_id)
#pass_update(pass_id, pass_name, route_num, stop_id, pass_phnum)
#attendant_update(attendant_phnum, content_list )

#[[length_route, capacity], [attendant_name], [driver_name, contact], [conductor_name, contact],[stop_id, number of passengers]]
