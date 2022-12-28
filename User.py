import DB2
def getUserCredentials():
    username=input("Enter username:")
    password=input("Enter password:")
    return username,password

def createUser():
    name=input("Enter name:")
    username=input("Enter user id:")
    password=input("Enter password:")
    return name,username,password

def userPanel(username):
    while True:
        print("---------------------------------------------------------------------------------")
        print("|                                User Dashboard                                 |")
        print("---------------------------------------------------------------------------------")
        print("1)Search Flight\n2)Book\n3)View my bookings\n4)Logout")
        inp=int(input())
        if inp==1:
            print("1)Search by date\n2)Search by flight time")
            choice=int(input("Enter your choice:"))
            if choice==1:
                date=input("Enter flight date:")
                DB2.viewFlightByDate(date)
            else:
                time=input("Enter flight time:")
                DB2.viewFlightByTime(time)
        elif inp==2:
            flight_no=int(input("Enter flight number to book:"))
            seats=int(input("Enter the number of seats:"))
            if DB2.bookFlight(username,flight_no,seats):
                print(str(seats)+" seats booked successly..!")
        elif inp==3:
            DB2.viewUserBooking(username)
        else:
            break