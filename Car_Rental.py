global did
global userid


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
        pass
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

# def Update_car():
#     global dealerid
#     carid=input("Enter Car ID: ")
#     dlt="update on cars where car_id='"+carid+"' and car_dealerid='"+str(dealerid)+"'"
#     c.execute(dlt)
#     conn.commit()
#     print("Car details deleted....")
#     initdealer()



    


        

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


def inituser():
    global userid
    print("""
            1.View All Cars
            2.search Cars
            3.Update Profile
            4.Logout

""")
    userc1=int(input("Enter The User Choice "))
    if userc1==1:
        userview()
    elif userc1==2:
        car_from=input("Enter Car From: ")
        car_to=input("Enter Car To: ")
        userview(car_from,car_to)
    elif userc1==3:
        pass
    elif userc1==4:
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
        pass
    elif userc==6:
        exit()
    
init()
    

