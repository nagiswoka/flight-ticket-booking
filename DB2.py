import ibm_db

conn = ibm_db.connect("","", "")
if conn :
    print('connected')
else:
    print("failed to connect")

Server = ibm_db.server_info(conn)


    
def createUser(name, user_id,password):
    stmt = "insert into User (name , user_id , password) values ('"+name+"','"+user_id+"','"+password+"');"
    if ibm_db.exec_immediate(conn, stmt):
        return True
    else:
        return False

def loginUser(user_id, password):
    stmt = ibm_db.exec_immediate(conn, "select password from user where user_id='"+user_id+"';")
    entries = 0
    while ibm_db.fetch_row(stmt) != False:
        entries += 1
        value = ibm_db.result(stmt, 0)
        print("Password: ", value)
        DBpassword = value
        if DBpassword != password:
            return False
        else:            
            return True

def adminLogin(username,password):
    stmt=ibm_db.exec_immediate(conn,"select password from ADMIN where username='"+username+"';")
    entries = 0
    while ibm_db.fetch_row(stmt) != False:
        entries += 1
        value = ibm_db.result(stmt, 0)
        DBpassword = value
        if DBpassword != password:
            return False
        else:            
            return True

def createAdmin(username,password):
    stmt = "insert into ADMIN (username,password) values ('"+username+"','"+password+"');"
    if ibm_db.exec_immediate(conn, stmt):
        return True
    else:
        return False


def addFlight(flight_no,flight_time,flight_date,start,dest):
    stmt = "insert into Flight (flight_no,flight_time,flight_date,start,dest) values ('"+str(flight_no)+"','"+flight_time+"','"+flight_date+"','"+start+"','"+dest+"');"
    if ibm_db.exec_immediate(conn,stmt):
        return True
    else:
        return False

def viewFlightByDate(date):
    sql= "select * from flight where flight_date='"+date+"';"
    stmt=ibm_db.exec_immediate(conn,sql)
    dictionary = ibm_db.fetch_both(stmt)
    print("-------------------------------------------------------------------------------------")
    print("| Flight Number | Flight Time | Flight Date |      Start      |      Destination    |")
    print("-------------------------------------------------------------------------------------")
    while dictionary != False:
        print("|{:15s}|{:13s}|{:13s}|{:17s}|{:21s}|".format( str(dictionary[1]),dictionary[2],dictionary[3],dictionary[4],dictionary[5] )) 
        print("-------------------------------------------------------------------------------------")
        dictionary = ibm_db.fetch_both(stmt)

def viewFlightByTime(time):
    sql= "select * from flight where flight_time='"+time+"';"
    stmt=ibm_db.exec_immediate(conn,sql)
    dictionary = ibm_db.fetch_both(stmt)
    print("-------------------------------------------------------------------------------------")
    print("| Flight Number | Flight Time | Flight Date |      Start      |      Destination    |")
    print("-------------------------------------------------------------------------------------")
    while dictionary != False:
        print("|{:15s}|{:13s}|{:13s}|{:17s}|{:21s}|".format( str(dictionary[1]),dictionary[2],dictionary[3],dictionary[4],dictionary[5] )) 
        print("-------------------------------------------------------------------------------------")
        dictionary = ibm_db.fetch_both(stmt)


def removeFlight(flight_no):
    stmt = "delete from flight where flight_no='"+flight_no+"';"
    if ibm_db.exec_immediate(conn,stmt):
        return True
    else:
        return False

def viewUserBooking(user_id):
    sql= "select * from booking where user_id='"+user_id+"';"
    stmt=ibm_db.exec_immediate(conn,sql)
    dictionary = ibm_db.fetch_both(stmt)
    print("----------------------------------------------------------------------------------------------------")
    print("| Flight Number | Flight Time | Flight Date |      Start      |      Destination    | Seats Booked |")
    print("----------------------------------------------------------------------------------------------------")
    while dictionary != False:
        print("|{:15s}|{:13s}|{:13s}|{:17s}|{:21s}|{:15s}".format( str(dictionary[1]),dictionary[2],dictionary[3],dictionary[4],dictionary[5],str(dictionary[6]) )) 
        print("----------------------------------------------------------------------------------------------------")
        dictionary = ibm_db.fetch_both(stmt)


def viewBookingsByNo(flight_no):
    sql= "select * from booking where flight_no='"+str(flight_no)+"';"
    stmt=ibm_db.exec_immediate(conn,sql)
    dictionary = ibm_db.fetch_both(stmt)
    while dictionary != False:
        user_id=dictionary[0]
        stmt=ibm_db.exec_immediate(conn,"select name from user where user_id='"+user_id+"';")
        dictionary = ibm_db.fetch_both(stmt)
        name=dictionary[0]
        print("----------------------------------------------------------------------------")
        print("|     Booked Person Name                     |          No of Seats        |")
        print("----------------------------------------------------------------------------")
        while dictionary != False:
                sql= "select seat from booking where user_id='"+user_id+"';"
                stmt=ibm_db.exec_immediate(conn,sql)
                dictionary = ibm_db.fetch_both(stmt)
                print("|{:44s}|{:29s}".format(name,str(dictionary[0])))
                print("----------------------------------------------------------------------------")
                dictionary = ibm_db.fetch_both(stmt)
        dictionary = ibm_db.fetch_both(stmt)

def viewBookingByTime(flight_time):
    sql="select * from Booking where flight_time='"+flight_time+"';"
    stmt=ibm_db.exec_immediate(conn,sql)
    dictionary = ibm_db.fetch_both(stmt)
    while dictionary != False:
        user_id=dictionary[0]
        stmt=ibm_db.exec_immediate(conn,"select name from user where user_id='"+user_id+"';")
        dictionary = ibm_db.fetch_both(stmt)
        name=dictionary[0]
        print("----------------------------------------------------------------------------")
        print("|     Booked Person Name                     |          No of Seats        |")
        print("----------------------------------------------------------------------------")
        while dictionary != False:
                sql= "select seat from booking where user_id='"+user_id+"';"
                stmt=ibm_db.exec_immediate(conn,sql)
                dictionary = ibm_db.fetch_both(stmt)
                print("|{:44s}|{:29s}".format(name,str(dictionary[0])))
                print("----------------------------------------------------------------------------")
                dictionary = ibm_db.fetch_both(stmt)
        dictionary = ibm_db.fetch_both(stmt)

def bookFlight(user_id,flight_no,seats):
    sql= "select * from flight where flight_no='"+str(flight_no)+"';"
    stmt=ibm_db.exec_immediate(conn,sql)
    dictionary = ibm_db.fetch_both(stmt)
    flight_date=""
    flight_time=""
    start=""
    dest=""
    while dictionary != False:
        flight_time=dictionary[1]
        flight_date=dictionary[2]
        start=dictionary[3]
        dest=dictionary[4]
        dictionary = ibm_db.fetch_both(stmt)
    stmt = "insert into Booking (user_id,flight_no,flight_time,flight_date,start,dest,seat) values ('"+user_id+"','"+str(flight_no)+"','"+flight_time+"','"+flight_date+"','"+start+"','"+dest+"','"+str(seats)+"');"
    if ibm_db.exec_immediate(conn,stmt):
        return True
    else:
        return False