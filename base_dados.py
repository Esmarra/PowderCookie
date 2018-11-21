# Program Name :	Music_for_all
# Base Language:	English
# Created by   :	Esmarra
# Creation Date:	20/11/2018
# Rework date entries:
# 		17/07/2018 : db_query refined
# Program Objectives:
# Observations:
# Special Thanks:
version ="alfa 0.01"

# ==== Imports ===== #
import os # to use cls
import getpass # masks password
import sys # exit clean

from db_query import *

# ==== Functions ==== #
# Clears Console
def cls(): os.system("CLS")

# User Register
def register():
	cls();
	print(" ==== User Register ==== ")
	name=input(">What's your Name:")
	user=input(">Type Username:")
	password=getpass.getpass(">Type Password:")
	edit=input(">Are you an editor?(y/n):")
	if edit=="y":
		user_level="admin"

	if(register_user(name,user,password,edit)==False):
		cls()
		print(" That Username is arleady Taken please try again")
	else:
		cls()
		print(" Success, Welcome %s"%user)
# User Login
def login():
	cls();
	print(" ==== User Login ==== ")
	user=input(">Type Username:")
	password=getpass.getpass(">Type Password:")
	if(get_user(user,password,"l")==True):
		print("User Validaded, Welcome %s"%user)
	else:
		print("Invalid User...")
		reg=input(">Register now?(y/n):")
		if reg=="y":
			register()

# Pre Clean Up
cls();
print(" ==== Version: %s ==== "%version)
ans=True
while ans:
	print ("""
		1.Login
		2.Register
		3.Add Music
		4.Exit
		""")
	ans=input(">Please select an option: ")
	if ans=="1":
		login();
	elif ans=="2":
		register();
		#Call Register
	elif ans=="3":
		cls();
		# Call Add_Music
	elif ans=="4":
		cls();
		print("Goodbye")
		sys.exit()
	elif ans !="":
		cls();
		print("\n Not Valid Choice Try again")



