global did
global userid
global adminid


import sqlite3 as sq
conn=sq.connect("Carbookings.db")
c=conn.cursor()
try:
    conn.execute("""create table if not exists admin 
                 (admin_id integer primary key,
                 admin_username varchar(20) not null,
                 admin_password varchar(20) not null)""")
    conn.execute('''create table if not exists car_dealers 
                 (car_dealarid integer primary key,
                 car_dealername varchar (20) not null,
                 car_dealerpassword varchar(20) not null,
                 car_dealermail varchar(20) not null,
                 car_dealerphone varchar(20) not null)''')
    conn.execute('''create table if not exists cars
                 (car_id integer primary key,
                 car_name varchar(20) not null,
                 car_type varchar(20) not null,
                 car_model varchar(20) not null,
                 car_dealerid int(11) not null,
                 car_from varchar(20) not null,
                 car_to varchar(20) not null),
                 car_number varchar(20) not null''')
    conn.execute('''create table if not exists users
                 (user_id integer primary key,
                 user_name varchar(20) not null,
                 user_password varchar(20) not null,
                 user_email varchar(20) not null,
                 user_phone varchar(20) not null)''')
    
except:
    print("some error")

# def add_admin():
#     global adminid
#     adminname=input("Enter The ADmin Name: ")
#     adminpass=input("Enter The Admin Password: ")
#     ins="""insert into admin(admin_username,admin_password) values
#     ('{}','{}')""".format(adminname,adminpass)
#     c.execute(ins)
#     conn.commit()
#     print("Admin Added....")
#     adminLogin()

def adminLogin():
    global adminid
    admin_username=input("Enter The Name: ")
    admin_password=input("Enter The Password: ")
    data=c.execute("select * from admin where admin_username='"+admin_username+"' and admin_password='"+admin_password+"'")
    d=data.fetchall()
    for i in d:
        adminid=i[0]
    t=len(d)
    if t==1:
        print("Login Successfull...")
        initadmin()
    else:
        print("Invalid Username and Password!...")
        adminLogin()

def veiwallusers():
    print("{0:10}{1:15}{2:18}{3:15}".format("user id","user name","user email","user phone"))
    data="select * from users"
    adata=c.execute(data)
    fchall=adata.fetchall()
    for i in fchall:
        print("{0:^5}{1:^15}{2:^18}{3:^15}".format(i[0],i[1],i[3],i[4]))
    adminc=int(input("Ener 1 to Delete : "))
    if adminc==1:
        userID=input("Enter The User Id: ")
        deldata="delete from users where user_id='"+str(userID)+"'"
        c.execute(deldata)
        conn.commit()
        print("User Deleted.....")
        initadmin()
    else:
        initadmin()

def viewall_dealers():
    print("{0:10}{1:15}{2:18}{3:15}".format("car_dealerid","car_dealername","car_dealeremail","car_dealerphone"))
    data="select * from car_dealers"
    adata=c.execute(data)
    fchall=adata.fetchall()
    for i in fchall:
        print("{0:^5}{1:^15}{2:^18}{3:^15}".format(i[0],i[1],i[3],i[4]))
    adminc=int(input("Ener 1 to Delete : "))
    if adminc==1:
        userID=input("Enter The User Id: ")
        deldata="delete from car_dealers where car_dealarid='"+str(userID)+"'"
        c.execute(deldata)
        conn.commit()
        print("Car Dealer Deleted.....")
        initadmin()
    else:
        initadmin()

def view_allcars():
    data=("select * from cars ")
    cabdata=c.execute(data)
    fn=cabdata.fetchall()
    #print("{0:15}{1:15}{2:15}{3:15}{4:15}{5:15}{6:15}".format("car name,car type,car model,car dealer id,car from,car to,car number"))
    for i in fn:
        print("{0:<15}{1:<15}{2:<15}{3:<15}{4:<15}{5:<15}{6:<15}".format(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
    adminc=int(input("Ener 1 to Delete : "))
    if adminc==1:
        userID=input("Enter The User Id: ")
        deldata="delete from cars where car_id='"+str(userID)+"'"
        c.execute(deldata)
        conn.commit()
        print("Car Deleted.....")
        initadmin()
    else:
        initadmin()

def admin_pwd_nm():
    global adminid
    oldPass=input("Enter The Old Password: ")
    data=c.execute("select * from admin where admin_password='"+oldPass+"' and admin_id='"+str(adminid)+"' ")
    d=data.fetchall()
    t=len(d)
    if t==1:
        newPass=input("Enter The New Password: ")
        conPass=input("Enter Confirm Password: ")
        if (newPass==conPass):
            updt="update admin set admin_password='"+newPass+"' where admin_id='"+str(adminid)+"'"
            c.execute(updt)
            conn.commit()
            print("New Password Added.....")
            initadmin()
        else:
            print("New Password and Confirm Password Not Matched!...")
            initadmin()

    else:
        print("Invalid Old Password!..")
        initadmin()

            

 




def initadmin():
    global adminid

    print("""
          1.View All Users
          2.View All Dealers
          3.View Cars
          4.Change Password
          5.Logout

""")
    uc=int(input("Enter Your Choice "))
    if uc==1:
        veiwallusers()
    elif uc==2:
        viewall_dealers()
    elif uc==3:
        view_allcars()
    elif uc==4:
        admin_pwd_nm()
    elif uc==5:
        del adminid
        init()




def dealerlog():
    global did
    car_dealername=input("Enter The Name: ")
    car_dealerpassword=input("Enter The Password: ")
    data=c.execute("select * from car_dealers where car_dealername='"+car_dealername+"' and car_dealerpassword='"+car_dealerpassword+"'")
    d=data.fetchall()
    for i in d:
        did=i[0]
    t=len(d)
    if (t==1):
        print("Login Successfull")
        initdealer()
    else:
        print("Invalid Username and password")
        dealerlog()

def initdealer():
    global did
    print("""
              1.Add Cars
              2.View Cars
              3.Delete Cars
              4.Update Cars
              5.Logout

""")
    dlrc=int(input("Enter The Dealer Choice : "))
    if dlrc==1:
        addcars()
    elif dlrc==2:
        view_cars()
    elif dlrc==3:
        del_car()
    elif dlrc==4:
        Update_car()
    elif dlrc==5:
        del did
        init()

def addcars():
    global did
    car_name=input("Enter The Car Name: ")
    car_type=input("Enter The Car Type: ")
    car_model=input("Enter The Car Model: ")
    car_dealerid=did
    car_from=input("Enter The Car To: ")
    car_to=input("Enter The Car To: ")
    car_number=input("Enter The Car Number: ")
    ins="""insert into cars(car_name,car_type,car_model,car_dealerid,car_from,car_to,car_number) values
    ('{}','{}','{}','{}','{}','{}','{}')""".format(car_name,car_type,car_model,str(car_dealerid),car_from,car_to,car_number)
    c.execute(ins)
    conn.commit()
    print("Car details added")
    initdealer()

def view_cars():
    global did
    data=("select * from cars where car_dealerid='"+str(did)+"'")
    cabdata=c.execute(data)
    fn=cabdata.fetchall()
    #print("{0:15}{1:15}{2:15}{3:15}{4:15}{5:15}{6:15}".format("car name,car type,car model,car dealer id,car from,car to,car number"))
    for i in fn:
        print("{0:<15}{1:<15}{2:<15}{3:<15}{4:<15}{5:<15}{6:<15}".format(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
        initdealer()

def del_car():
    global did
    carid=input("Enter Car ID: ")
    dlt="delete from cars where car_id='"+carid+"' and car_dealerid='"+str(did)+"'"
    c.execute(dlt)
    conn.commit()
    print("Car details deleted....")
    initdealer()

def Update_car():
    global did
    car_name=input("Enter Car Name: ")
    car_type=input("Enter Car Tpye: ")
    car_model=input("Enter Car Model: ")
    car_from=input("Enter Car From: ")
    car_to=input("Enter Car To: ")
    car_number=input("Enter Car Number: ")
    dlt="update cars set car_name='"+car_name+"',car_type='"+car_type+"',car_model='"+car_model+"',car_from='"+car_from+"',car_to='"+car_to+"',car_number='"+car_number+"' where car_dealerid='"+str(did)+"'"
    c.execute(dlt)
    conn.commit()
    print("Car details Updated....")
    initdealer()
    
    
def userreg():
    user_name=input("Enter Your Name: ")
    user_password=input("Enter Your Password: ")
    user_email=input("Emter Your Email: ")
    user_phone=input("Enter Your Phone Number: ")
    data=c.execute("select * from users where user_email='"+user_email+"'")
    t=len(data.fetchall())
    if (t==0):
        ins="""insert into users(
        user_name,user_password,user_email,user_phone) values
        ('{}','{}','{}','{}')""".format(user_name,user_password,user_email,user_phone)
        c.execute(ins)
        conn.commit()
        print("User Created....")
        init()
    else:
        print("User email Already Exits.... ")
        dealerreg()

def userlog():
    global userid
    username=input("Enter The Name: ")
    userpassword=input("Enter The Password: ")
    data=c.execute("select * from users where user_name='"+username+"' and user_password='"+userpassword+"'")
    d=data.fetchall()
    for i in d:
        userid=i[0]
    t=len(d)
    if (t==1):
        print("Login Successfull")
        inituser()
    else:
        print("Invalid Username and password")
        userlog()

def userview(car_from="",car_to=""):
    if car_from !="" and car_to !="":
        data=("select * from cars where car_from='"+car_from+"' and car_to='"+car_to+"' ")
        cabdata=c.execute(data)
        fn=cabdata.fetchall()
        for i in fn:
            print(i)
            inituser()
    else:
        data=("select * from cars ")
        cabdata=c.execute(data)
        fn=cabdata.fetchall()
        #print("{0:15}{1:15}{2:15}{3:15}{4:15}{5:15}{6:15}".format("car name,car type,car model,car dealer id,car from,car to,car number"))
        for i in fn:
            print("{0:<15}{1:<15}{2:<15}{3:<15}{4:<15}{5:<15}{6:<15}".format(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
            inituser()

def user_update():
    global userid
    user_email=input("Enter the Email: ")
    user_Phone=input("Enter the Phone Number: ")
    updt="update users set user_email='"+user_email+"',user_phone='"+user_Phone+"' where user_id='"+str(userid)+"'"
    c.execute(updt)
    conn.commit()
    print("User Profile Updated....")
    inituser()

def changePass():
    global userid
    oldPass=input("Enter The Old Password: ")
    data=c.execute("select * from users where user_password='"+oldPass+"' and user_id='"+str(userid)+"' ")
    d=data.fetchall()
    t=len(d)
    if t==1:
        newPass=input("Enter The New Password: ")
        conPass=input("Enter Confirm Password: ")
        if (newPass==conPass):
            updt="update users set user_password='"+newPass+"' where user_id='"+str(userid)+"'"
            c.execute(updt)
            conn.commit()
            print("New Password Added.....")
            inituser()
        else:
            print("New Password and Confirm Password Not Matched!...")
            inituser()

    else:
        print("Invalid Old Password!..")
        inituser()



def inituser():
    global userid
    print("""
            1.View All Cars
            2.search Cars
            3.Update Profile
            4.Change Password
            5.Logout

""")
    userc1=int(input("Enter The User Choice "))
    if userc1==1:
        userview()
    elif userc1==2:
        car_from=input("Enter Car From: ")
        car_to=input("Enter Car To: ")
        userview(car_from,car_to)
    elif userc1==3:
        user_update()
    elif userc1==4:
        changePass()
    elif userc1==5:
        del userid
        init()



def dealerreg():
    car_dealername=input("Enter The Name: ")
    car_dealerpassword=input("Enter The Password: ")
    car_dealermail=input("Enter The Mail: ")
    car_dealerphone=input("Enter Phone Number: ")
    ins="""insert into car_dealers (car_dealername,car_dealerpassword,car_dealermail,car_dealerphone) values
    ('{}','{}','{}','{}')""".format(car_dealername,car_dealerpassword,car_dealermail,car_dealerphone)
    c.execute(ins)
    conn.commit()
    init()


def init():
    print("""

          1.Dealer Registration
          2.Dealer Login
          3.User Registration
          4.User Login
          5.Admin Login
          6.Exit
        
""")
    
    userc=int(input("Enter Your Choice: "))
    if userc==1:
        dealerreg()
    elif userc==2:
        dealerlog()
    elif userc==3:
        userreg()
    elif userc==4:
        userlog()
    
    elif userc==5:
        adminLogin()
    elif userc==6:
        exit()
    
init()
    

