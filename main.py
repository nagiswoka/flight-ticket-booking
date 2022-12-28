import Admin,User,DB2
while True:
    print("---------------------------------------------------------------------------------")
    print("|                         Welcome to Fly Airlines                               |")
    print("---------------------------------------------------------------------------------")
    print("Log in as:\n1)Admin\n2)User\nNew user or admin..?\n3)Signup as user\n4)Signup as admin\n5)Exit")
    inp=int(input())
    if inp==1:
        username,password=Admin.getAdminCredentials()
        if DB2.adminLogin(username,password):
            Admin.adminPanel()
        else:
            print("Problem with server.Try again later..!")
    elif inp==2:
        username,password=User.getUserCredentials()
        if DB2.loginUser(username,password):
            User.userPanel(username)
        else:
            print("Problem with server.Try again later..!")
    elif inp==3:
        name,user_id,password=User.createUser()
        if DB2.createUser(name,user_id,password):
            print("User created Successfully..!")
        else:
            print("Problem with server.Try again later..!")
    elif inp==4:
        username,password=Admin.getAdminCredentials()
        if DB2.createAdmin(username,password):
            print("Admin created Successfully..!")
        else:
            print("Problem with server.Try again later..!")
    else:
        break