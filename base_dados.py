# Program Name :	Music_for_all
# Base Language:	English
# Created by   :	Esmarra
# Creation Date:	20/11/2018
# Rework date entries:
# 		17/07/2018 : db_query refined
# Program Objectives:
# Observations:
# Special Thanks:
version ="alfa0.01"

# ==== Imports ===== #
import os # to use cls
import getpass # masks password
import sys # exit clean
import time #sleep

from db_query import *

# ==== Global Vars ==== #
global user
user=None

# ==== Functions ==== #
# Clears Console
def cls(): os.system("CLS")

# User Register
def register():
	global user
	print(" ==== User Register ==== ")
	name=input(">What's your Name:")
	user=input(">Type Username:")
	password=getpass.getpass(">Type Password:")
	edit=input(">Are you an editor?(y/n):")
	if edit=="y":
		user_level="editor"
	else:
		user_level="user"
	if(register_user(name,user,password,user_level)==False):
		cls()
		print(" That Username is arleady Taken please try again")
		register()
	else:
		cls()
		print(" Success, Welcome %s"%user)

# User Login
def login():
	global user
	cls();
	print(" ==== User Login ==== ")
	user=input(">Type Username:")
	password=getpass.getpass(">Type Password:")
	if(get_user(user,password,"l")==True):
		print("\n User Validaded, Welcome %s "%user)
		print("\n Logging you in... Please wait")
		time.sleep(1.5) 
		cls()
	else:
		print("Invalid User...")
		reg=input(">Register now?(y/n):")
		if reg=="y":
			cls();
			register()

# Add Music
# def add_music():
	# if()
	

# Pre Clean Up
cls();
ans=True
while ans:
	user="esmr"
	try:
		print ("""	_______________________________
		 Version:%s
		 User:%s            
		 
		+-------------+
		| 1.Login     |
		+-------------+
		| 2.Register  |
		+-------------+
		| 3.Add Music |
		+-------------+
		| 4.Exit      |
		+-------------+
	_______________________________
			"""%(version,user))
		ans=input(">Please select an option: ")
		if ans=="1":
			login();
		elif ans=="2":
			cls();
			register();
			#Call Register
		elif ans=="3":
			cls();
			if user != None:
				if user_lvl(user)=="editor" or user_lvl(user)=="admin" :
					#call add music
					print("yay")
				else:
					print("You are not an editor")

			else:
				print("Please Login");
			# Call Add_Music
		elif ans=="4":
			cls();
			print("Goodbye")
			sys.exit()
		elif ans !="":
			cls();
			print("\n Not Valid Choice Try again")
	
	except KeyboardInterrupt:
		sys.exit()