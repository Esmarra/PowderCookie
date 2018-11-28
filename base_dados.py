# Program Name :	Music_for_all program
# Base Language:	MixedEnglish
# Created by   :	Esmarra
# Creation Date:	20/11/2018
# Rework date entries:
# Program Objectives:
# Observations:
# Special Thanks:
version ="Alfa0.5"

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

####======== Functions ========####
# Clears Console
def cls(): os.system("CLS")

##========= Console Inputs ========##
#|---- User Register ----|
def register():
	global user
	print(" ==== User Register ==== ")
	name=input("> What's your Name:")
	user=input("> Type Username:")
	password=getpass.getpass(">Type Password:")
	edit=input("> Are you an editor?(y/n):")
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

#|---- User Login ----|
def login():
	global user
	cls();
	print(" ==== User Login ==== ")
	user=input("> Type Username:")
	password=getpass.getpass("> Type Password:")
	if(get_user(user,password,"l")==True):
		print("\n User Validaded, Welcome %s "%user)
		print("\n Logging you in... Please wait")
		time.sleep(1.5) 
		cls()
	else:
		print("\n> Wrong Username or Password, try again")
		print("""
    1 - Login
    2 - Register
		""")
		opt=input("> Please select an option: ")
		if opt=="1":
			cls()
			login()
		elif opt=="2":
			cls();
			register()
		elif opt !="":
			cls()
			return

#|---- Add Music ----|
def add_music():
	print("\n ==== Add Music ==== ")
	#FK1 Check --> criar def fk_autor
	nome_autor=None
	c=0;
	while (autor_check(nome_autor)==False):
		if(c!=0):print(" ERROR, Type Music Author Again!")
		nome_autor=input("> Type Music Author:")
		if(c>0):
			print("""
Author not present in Database
	1 - List Author's in Database
	2 - Try Again
	3 - Add New Author
			""")
			opt=input("> Please select an option: ")
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
	
	#FK2 Check --> criar def fk_composer
	nome_comp=None
	c=0
	while (composer_check(nome_comp)==False):
		if(c!=0):print(" ERROR, Type Music Composer Again!")
		nome_comp=input(">Type Music Composer:")
		if(c>0):
			print("""
Composer not present in Database
	1 - List Composer's in Database
	2 - Try Again
	3 - Add New Composer
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
	
#|---- Add Autor ----|
def add_autor():
	print(" ==== Add Author ==== ")
	nome_autor=input("> Type Author Name: ")
	if(autor_check(nome_autor)!=False):
		print(" Author already in database")
		return
	#Continue
	historia=input("> Type Author History: ")
	return insert_autor(nome_autor,historia)

#|---- Add Composer ----|
def add_composer():
	print(" ==== Add Composer ==== ")
	nome_comp=input("> Type Composer Name: ")
	if(composer_check(nome_comp)!=False):
		print(" Composer already in database")
		return
	#Continue
	genero=input("> Type Composer Genre: ")
	print(">>Enter Composer Birth Date<<")
	birth_date=input("  Year: ")
	birth_date+='-'
	birth_date+=input("  Month: ")
	birth_date+='-'
	birth_date+=input("  Day: ")
	return insert_comp(nome_comp,genero,birth_date)

#|---- Add Album ----|
def add_album():
	print(" ==== Add Album ==== ")
	#FK CHECK
	nome_autor=None
	c=0;
	while (autor_check(nome_autor)==False):
		if(c!=0):print(" ERROR, Type Album Author Again!")
		nome_autor=input("> Type Album Author: ")
		if(c>0):
			print("""
Author not present in Database
	1 - List Author's in Database
	2 - Try Again
	3 - Add New Author
			""")
			opt=input("> Please select an option: ")
			if opt=="1":
				cls()
				#Listar Autores
				list_autor()
				add_album()
			elif opt=="2":
				cls();
				add_album()
			elif opt=="3":
				cls();
				#Check FO
				if(add_autor()==True):
					print(" Author Insert Success")
					add_album()
			elif opt !="":
				cls()
				return
		c+=1
	#Continue, Duplicate Check
	nome_album=input("> Type Album Name: ")
	if(album_check(nome_album)!=False):
		print(" Album already in database")
		return
	#Continue, Insert Remaning Colums
	print("> Type Album Date: ")
	album_date=input("  Year: ")
	ano_album=album_date
	album_date+='-'
	album_date+=input("  Month: ")
	album_date+='-'
	album_date+=input("  Day: ")
	album_editora=input("> Enter label's name: ")

	return insert_album(nome_album, album_date, album_editora, ano_album, autor_check(nome_autor))

#|---- Add Review ----| BUG? ver se dá para tentar fazer 2 uploads a review
def add_review():	
	print(" ==== Add Review ==== ")
	#FK CHECK
	nome_album=None
	c=0;
	while (album_check(nome_album)==False):
		if(c!=0):print(" ERROR, Type Album Name Again!")
		nome_album=input("> Type Album Name: ")
		if(c>0):
			print("""
Album not present in Database
	1 - List Album's in Database
	2 - Try Again
	3 - Add New Album
			""")
			opt=input("> Please select an option: ")
			if opt=="1":
				cls()
				#Listar Album
				list_album()
				add_review()
			elif opt=="2":
				cls();
				add_review()
			elif opt=="3":
				cls();
				#Check FO
				if(add_album()==True):
					print(" Album Insert Success")
					add_review()
			elif opt !="":
				cls()
				return
		c+=1

	review=input("> Type Review: ")
	rating=input("> Type rating from 1 to 5: ")
	while (int(rating) < 1 or int(rating) > 5):
		print(" ERROR ")
		rating=input("> Type rating from 1 to 5: ")
	
	return insert_review(review,int(rating),album_check(nome_album),check_user(user))

#|---- Add Playlist  ----| BUG falta duplicate check (query user e pl_nome) 
def add_playlist():
	print(" ==== Add Playlist ==== ")
	#Check Duplicate? pois tá parado Manel...
	nome_playlist=input("> Type Playlist Name: ")
	if(playlist_check(nome_playlist)!=False):
		print(" Playlist Already in database")
		return
	privacidade=input("> Is The Playlist private?(y/n): ")
	if privacidade=="y":
		pl_priv="1"
	else:
		pl_priv="0"
	
	return insert_playlist(nome_playlist, pl_priv, check_user(user))

#|---- Add Membros  ----|
def add_membro():
	print(" ==== Add Membro ==== ")
	#FK CHECK
	nome_autor=None
	c=0;
	while (autor_check(nome_autor)==False):
		if(c!=0):print(" ERROR, Type Author/Band Name Again!")
		nome_autor=input("> Type Author/Band Name: ")
		if(c>0):
			print("""
Author not present in Database
	1 - List Author's in Database
	2 - Try Again
	3 - Add New Author
			""")
			opt=input("> Please select an option: ")
			if opt=="1":
				cls()
				#Listar Autores
				list_autor()
				add_membro()
			elif opt=="2":
				cls();
				add_membro()
			elif opt=="3":
				cls();
				#Check FO
				if(add_autor()==True):
					print(" Author Insert Success")
					add_membro()
			elif opt !="":
				cls()
				return
		c+=1
	
	nome_membro=input("> Type Membro Name: ")
	if(membro_check(nome_membro)!=False):
		print(" Member Already in database")
		return
	historia_membro=input("> Type Membros History: ")
	print("> Type Data de Nascimento do Membro: ")
	membro_date=input("  Year: ")
	membro_date+='-'
	membro_date+=input("  Month: ")
	membro_date+='-'
	membro_date+=input("  Day: ")
	
	return insert_membro(nome_membro, historia_membro, membro_date, autor_check(nome_autor))

#|---- Add Concerto  ----|
def add_concerto():
	print(" ==== Add Concerto ==== ")
	#FK CHECK
	nome_autor=None
	c=0;
	while (autor_check(nome_autor)==False):
		if(c!=0):print(" ERROR, Type Author/Band Name Again!")
		nome_autor=input("> Type Author/Band Name: ")
		if(c>0):
			print("""
Author not present in Database
	1 - List Author's in Database
	2 - Try Again
	3 - Add New Author
			""")
			opt=input("> Please select an option: ")
			if opt=="1":
				cls()
				#Listar Autores
				list_autor()
				add_concerto()
			elif opt=="2":
				cls();
				add_concerto()
			elif opt=="3":
				cls();
				#Check FO
				if(add_autor()==True):
					print(" Author Insert Success")
					add_concerto()
			elif opt !="":
				cls()
				return
		c+=1
	
	sitio_concerto=input("> Type Concert Location: ")
	print("> Type Concert Date: ")
	concerto_date=input("  Year: ")
	concerto_date+='-'
	concerto_date+=input("  Month: ")
	concerto_date+='-'
	concerto_date+=input("  Day: ")
	
	return insert_concerto(sitio_concerto, concerto_date, autor_check(nome_autor))

#|---- Search Music  ----|
def search_music():
	global user
	print(" ==== Search_Music ==== ")
	nome_musica=input("> Type Music Name: ")
	
	nome_autor=input("> Type Author Name: ")
	#Write Music Id to array ?? OVERKILL
	music_array=lookup_music(nome_musica,nome_autor)
	
	if(array==[]):
		cls()
		print(" No Match for Search: '%s' Listing All Musics\n"%nome_musica)
		list_music()
		return
	ans=True
	while ans:
		try:
			print("""
What do you Want to do?
    1 - Add Music to Playlist
    2 - Search Another Music
    3 - Back to Main Menu
			""")
			ans=input("> Please select an option: ")
			if ans=="1":
				#Pergunta Publica ou Privada
				priv=input("Adicionar a Uma Playlist Publica?(y/n)")
				if(priv=="y"):
					pl_array=list_playlist("publicas",check_user(user))
				else:
					pl_array=list_playlist("user",check_user(user))
				#Verificar se Playlist existe
				
				
				#list playlist?
				#select
				print("tbd")

			if ans=="2":
				cls()
				search_music()

			if ans=="3":
				return
		except KeyboardInterrupt:
			sys.exit()
search_music()
##======== MENUS ========##
def user_menu():
	global user
	cls();
	ans=True
	while ans:
		try:
			print ("""	_______________________________
	User: %s
		 
		+------------------+
		| 1.Search Music   |
		+------------------+
		| 2.Search Author  |
		+------------------+
		| 0.Logout         |
		+------------------+
		| q.Exit           |
		+------------------+
	Version: %s
	_______________________________
			"""%(user,version))
			ans=input("> Please select an option: ")
			if ans=="1":
				search_music()
				
			elif ans=="2":
				cls();
				#Call Register
				register();
				
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
				
			elif ans=="0":
				print("\n Logging you out... Please wait")
				time.sleep(1.5) 
				cls()
				user=None
				int_main();
				
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
	global user
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
		| 0.Logout    |
		+-------------+
		| q.Exit      |
		+-------------+
	Version: %s
	_______________________________
			"""%(user,version))
			ans=input("> Please select an option: ")
			if ans=="1":
				login();
			
			#Option -> Register
			elif ans=="2":
				cls();
				register();

			#Option -> ND
			elif ans=="3":
				cls();

			elif ans=="0":
				print("\n Logging you out... Please wait")
				time.sleep(1.5) 
				cls()
				user=None
				int_main();
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
				if user_lvl(user)=="editor":
					editor_menu()
				else :
					user_menu()
					
			elif ans=="q":
				cls();
				print("\n Goodbye \n")
				sys.exit()
			elif ans !="":
				cls();
				print("\n > Not A Valid Choice Try again")
		except KeyboardInterrupt:
			sys.exit()

##========  Test Code Here ========##
#int_main()
#user_menu()
#search_music()
