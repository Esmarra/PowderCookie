# Program Name :	Music_for_all
# Base Language:	MixedEnglish
# Created by   :	Esmarra
# Creation Date:	20/11/2018
# Rework date entries:
# 		22/11/2018 : db_query refined
#		25/11/2018 : password encryption (Only Hashed better than nothing i guess)
#							Created: add_music() add_autor() list_autor() autor_check() insert_autor()
#		26/11/2018 : Created: add_autor() list_autor() list_composer() composer_check()
#
# Program Objectives:
# Observations:
# Special Thanks:
version ="Alfa0.03"

# ==== Imports ===== #
import os # to use cls
import getpass # masks password
import sys # exit clean
import time #sleep

from db_query import *

# ==== Global Vars ==== #
global user
user=None
from cookies import * #APAGAR ISTO QUANDO ENVIAR AO PROF

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
		print("\n>Wrong Username or Password, try again")
		print("""
    1 - Login
    2 - Register
		""")
		opt=input(">Please select an option: ")
		if opt=="1":
			cls()
			login()
		elif opt=="2":
			cls();
			register()
		elif opt !="":
			cls()
			return

# Add Music
def add_music():
	print("\n ==== Add Music ==== ")
	#VEREFY IF AUTHOR EXISTS [CRIAR VERIFY AUTHOR DEF]
	nome_autor=None
	c=0;
	while (autor_check(nome_autor)==False):
		if(c!=0):print(" ERRO, introduza novamente o Autor")
		nome_autor=input(">Type Music Author:")
		if(c>0):
			print("""
Autor Não Existente na base de dados
	1 - Ver Lista de Autores
	2 - Tertar Outra vez
	3 - Adicionar Novo Autor
			""")
			opt=input(">Please select an option: ")
			if opt=="1":
				cls()
				#Listar Autores
				list_autor()
				add_music()
			elif opt=="2":
				cls();
				add_music()
			elif opt=="3":
				cls();
				#Check FO
				if(add_autor()==True):
					print(" Author Insert Success")
					add_music()
			elif opt !="":
				cls()
				return
		c+=1
	
	# Verify if composer exists [CRIAR VERIFY COMPOSER DEF]
	nome_comp=None
	c=0
	while (composer_check(nome_comp)==False):
		if(c!=0):print(" ERRO, introduza novamente o Compositor")
		nome_comp=input(">Type Music Composer:")
		if(c>0):
			print("""
Compositor Não Existente na base de dados
	1 - Ver Lista de Compositor
	2 - Tertar Outra vez
	3 - Adicionar Novo Compositor
			""")
			opt=input(">Please select an option: ")
			if opt=="1":
				cls()
				#Listar Compositor
				list_composer()
			elif opt=="2":
				cls();
				add_music()
			elif opt=="3":
				cls();
				#Add author
				if(add_composer()==True):
					print(" Author Insert Success")
					add_music()
			elif opt !="":
				cls()
				return
		c+=1
		
	m_nome=input(">Type Music Name: ")
	m_genero=input(">Type Music Genre: ")
	letra=input(">Type Music Lyrics: ")
	m_time=input(">Type Music Time: ")
	choice=input(">Music has an album?(y/n):")
	if choice=="y":
		print("Codigo á espera do Manel")
		m_album=None
		flag='a'
	elif choice !="":
		m_album=None
		flag=''
	# Upload DB
	insert_music(m_nome,m_genero,letra,m_time,composer_check(nome_comp),album_check(m_album),autor_check(nome_autor),flag);
	return

# Add Autor
def add_autor():
	print(" ==== Add Author ==== ")
	nome_autor=input(">Type Composer Name:")
	if(autor_check(nome_autor)!=False):
		print(" Author Already in database")
		return
		#skip para update history?
	historia=input(">Type Author History:")
	return insert_autor(nome_autor,historia)

# Add Composer
def add_composer():
	print(" ==== Add Composer ==== ")
	nome_comp=input(">Type Composer Name: ")
	if(composer_check(nome_comp)!=False):
		print(" Composer Already in database")
		return
		#skip para update history?
	genero=input(">Type Composer Genre: ")
	print(">>Enter Composer Birth Date<<")
	birth_date=input("  Year: ")
	birth_date+='-'
	birth_date+=input("  Month: ")
	birth_date+='-'
	birth_date+=input("  Day: ")
	return insert_comp(nome_comp,genero,birth_date)

# ==== MENUS ==== #
def user_menu():
	cls();
	ans=True
	while ans:
		try:
			print ("""	_______________________________
	User: %s
		 
		+-------------+
		| 1.Login     |
		+-------------+
		| 2.Register  |
		+-------------+
		| 3.Add Music |
		+-------------+
		| 4.Logout    |
		+-------------+
		| q.Exit      |
		+-------------+
	Version: %s
	_______________________________
			"""%(user,version))
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
						add_music()
					else:
						print("You are not an editor")

				else:
					print("Please Login");
				# Call Add_Music
			elif ans=="q":
				cls();
				print("\n Goodbye \n")
				sys.exit()
			elif ans !="":
				cls();
				print("\n Not Valid Choice Try again")
		except KeyboardInterrupt:
			sys.exit()

def editor_menu():
	cls();
	ans=True
	while ans:
		try:
			print ("""	_______________________________
	User: %s
		 
		+-------------+
		| 1.Add Music |
		+-------------+
		| 2.Add Author|
		+-------------+
		| 4.Logout    |
		+-------------+
		| q.Exit      |
		+-------------+
	Version: %s
	_______________________________
			"""%(user,version))
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
						add_music()
					else:
						print("You are not an editor")

				else:
					print("Please Login");
				# Call Add_Music
			elif ans=="q":
				cls();
				print("\n Goodbye \n")
				sys.exit()
			elif ans !="":
				cls();
				print("\n Not Valid Choice Try again")
		except KeyboardInterrupt:
			sys.exit()

def int_main():
	# Pre Clean Up
	cls();
	ans=True
	while ans:
		try:
			print ("""	_______________________________
	User: %s

		+-------------+
		| 1.Login     |
		+-------------+
		| 2.Register  |
		+-------------+
		| q.Exit      |
		+-------------+

	       Version: %s"""%(user,version))
			print("""	_______________________________\n""")
			User="pedro"
			ans=input("> Please select an option: ")
			if ans=="1":
				login();
				#Read Userlvl from DB
				if user_lvl(user)=="editor":
					editor_menu()
				else :
					user_menu()
			elif ans=="2":
				cls();
				register();
				#
				login();
			elif ans=="q":
				cls();
				print("\n Goodbye \n")
				sys.exit()
			elif ans !="":
				cls();
				print("\n > Not A Valid Choice Try again")
		except KeyboardInterrupt:
			sys.exit()

int_main()
