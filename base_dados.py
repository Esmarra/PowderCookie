## BD MAIN PROGRAM ##
## 20/11
version ="alfa 0.01"

import os # to use cls
import getpass # masks password

from db_query import *

def cls(): os.system("CLS")

def register():
    print("registering")

def login():
    print("\nUser Login")
    user=input(">Type Username:")
    password=getpass.getpass(">Type Password:")
    if(get_user(user,password)==True):
        print("User Validaded, Welcome %s"%user)
    else:
        print("Invalid User...")
        reg=input(">Register now?(y/n):")
        if reg=="y":
            register()

# Pre Clean Up
cls();
print('==== Version: %s ===='%version)
ans=True
while ans:
    print ("""
    1.Login
    2.Register
    3.Add Music
    4.Open Music
    """)
    ans=input(">Please select an option: ")
    if ans=="1":
        cls();
        login();
    elif ans=="2":
        cls();
        print("\n Student Deleted") 
    elif ans=="3":
        cls();
        print("\n Student Record Found") 
    elif ans=="4":
        cls();
        print("\n Goodbye") 
    elif ans !="":
        cls();
        print("\n Not Valid Choice Try again")



