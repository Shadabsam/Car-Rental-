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
                 car_dealer int(11) not null,
                 car_from varchar(20) not null,
                 car_to varchar(20) not null)''')
    conn.execute('''create table if not exists users
                 (user_id integer primary key,
                 user_name varchar(20) not null,
                 user_password varchar(20) not null,
                 user_email varchar(20) not null,
                 user_phone varchar(20) not null)''')
    
except:
    print("some error")

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
    userc=int(input("Enter Your Choice "))
    if userc==1:
        dealerreg()
    elif userc==2:
        pass
    elif userc==3:
        userreg()
    elif userc==4:
        pass
    elif userc==5:
        pass
    elif userc==6:
        exit()

init()
    

