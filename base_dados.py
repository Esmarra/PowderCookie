# Program Name :	Music_for_all program
# Base Language:	MixedEnglish
# Created by   :	
# Creation Date:	20/11/2018
# Rework date entries:
# Program Objectives:
# Observations:
# Special Thanks:
version ="Beta1.0"

# ==== Imports ===== #
import os # to use cls
import getpass # masks password
import sys # exit clean
import time #sleep

from db_query import *

# ==== Global Vars ==== #
global user
user=None
#from cookies import * #APAGAR NA SUBMISSAO

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
	#Verifica se já existe esta musica na base de dados
	if(music_check(m_nome,autor_check(nome_autor))!=False):
		csl()
		print(" There is a Music From %s Author with Name = %s Try Again")
		return
	m_genero=input(">Type Music Genre: ")
	letra=input(">Type Music Lyrics: ")
	m_time=input(">Type Music Time: ")
	choice=input(">Music has an album?(y/n):")
	if choice=="y":
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
					add_music()
				elif opt=="2":
					cls();
					add_music()
				elif opt=="3":
					cls();
					#Check FO
				if(add_album()==True):
					print(" Album Insert Success")
					add_music()
				elif opt !="":
					cls()
					return
			c+=1
		flag='a'
	elif choice !="":
		nome_album=None
		flag=''
	# Upload DB
	insert_music(m_nome,m_genero,letra,m_time,composer_check(nome_comp),album_check(nome_album),autor_check(nome_autor),flag);
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

#|---- Add Review ----|
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

	#Duplicate Username Review Check
	if(check_review(album_check(nome_album),check_user(user))!=False):
		print(" Review Already in database")
		return
	review=input("> Type Review: ")
	rating=input("> Type rating from 1 to 5: ")
	while (int(rating) < 1 or int(rating) > 5):
		print(" ERROR ")
		rating=input("> Type rating from 1 to 5: ")
	
	return insert_review(review,int(rating),album_check(nome_album),check_user(user))
#add_review()

#|---- Add Playlist  ----|
def add_playlist():
	print(" ==== Add Playlist ==== ")
	nome_playlist=input("> Type Playlist Name: ")
	if(check_playlist(nome_playlist)!=False):
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

	if(music_array==[]):
		cls()
		print(" No Music Match for Name= '%s' & Author = '%s' \n Listing All Musics\n"%nome_musica)
		list_music()
		return

	ans=True
	while ans:
		try:
			print("""
What do you Want to do?
    1 - Add Music to Playlist
	2 - Add Music to Album
    3 - Search Another Music
    4 - Back to Main Menu
			""")
			ans=input("> Please select an option: ")
			if ans=="1":
				#Pergunta Publica ou Privada
				priv=input("Adicionar a Uma Playlist Publica?(y/n)")
				if(priv=="y"):
					pl_array=list_playlist("todas",check_user(user))
				else:
					pl_array=list_playlist("user",check_user(user))
				#print(pl_array)
				#Verificar se Playlist existe
				nome_playlist=None
				c=0;
				while (check_playlist(nome_playlist)==False):
					if(c!=0):print(" ERROR, Type Playlist Name Again!")
					nome_playlist=input("> Type Playlist Name:")
					if(c>0):
						print("""
Playlist not present in Database
    1 - List Playlist's in Database
    2 - Try Again
    3 - Add New Playlist
						""")
						opt=input("> Please select an option: ")
						if opt=="1":
							cls()
							#Listar Autores
							list_playlist("user",check_user(user))
							search_music()
						elif opt=="2":
							cls();
							search_music()
						elif opt=="3":
							cls();
							#Check FO
							if(add_playlist()==True):
								print(" Playlist Insert Success")
								search_music()
						elif opt !="":
							cls()
							return
					c+=1
				
				#Add Music to Playlist
				insert_playlist_music(pl_array[0],music_array[0])
				return

			if ans=="2":
				cls()
				#|---- Add Music Album  ----|
				print(" ==== Add_Music_Album ==== ")
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
				
				update_music_album(music_array[0],autor_check(nome_autor),album_check(nome_album))
				
			if ans=="3":
				cls()
				search_music()

			if ans=="4":
				return
		except KeyboardInterrupt:
			sys.exit()

#|---- Search autor  ----|
def search_autor():
	print(" ==== Search Author ==== ")
	c=0;
	nome_autor=input("> Type Author Name: ")
	a=autor_check(nome_autor)
		
	if(a==False):
		cls()
		print(" No Match for Search: '%s' Listing All Authors\n"%nome_autor)
		list_autor()
		return
	else: 
		lookup_autor(nome_autor)
	ans=True
	while ans:
		try:
			print("""
What do you Want to do?
    1 - Add Member to Autor
    2 - Search Another Author
    3 - Back to Main Menu
			""")
			ans=input("> Please select an option: ")
			if ans=="1":
				cls()
				#Verificar se Autor existe
				nome_autor=None
				c=0;
				while (autor_check(nome_autor)==False):
					if(c!=0):print(" ERROR, Type Autor Name Again!")
					nome_autor=input("> Type Autor Name:")
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
							search_autor()
						elif opt=="2":
							cls();
							search_autor()
						elif opt=="3":
							cls();
							#Check FO
							if(add_autor()==True):
								print(" Author Insert Success")
								search_autor()
						elif opt !="":
							cls()
							return
					c+=1
				
				#Add Member to Autor
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
				if(insert_membro(nome_membro, historia_membro, membro_date, autor_check(nome_autor))==True):print(" \n Member Successfully Inserted")
				
			return
			if ans=="2":
				cls()
				search_autor()
			if ans=="3":
				return
		except KeyboardInterrupt:
			sys.exit()

#|---- Search Album  ----|
def search_album():
	print(" ==== Search album ==== ")
	c=0;
	nome_album=input("> Type Album Name: ")
	nome_autor=input("> Type Album Author Name: ")
	album_array=lookup_album(nome_album,nome_autor)

	if(album_array==[]):
		cls()
		print(" No Album Match for Name= '%s' & Author = '%s' \n Listing All Albums\n"%(nome_album, nome_autor))
		list_album()
		return
	ans=True
	while ans:
		try:
			print("""
	1 - Add Review to Album
	2 - Search Another Album
	3 - Back to Main Menu
			""")
			ans=input("> Please select an option: ")
			if ans=="1":
				cls()
				if(add_review()==True):
					print(" Review Insert Success")
				user_menu()
			if ans=="3":
				cls()
				search_album()				
			if ans=="4":
				cls()
				return
		except KeyboardInterrupt:
			sys.exit()

#|---- Search Concerto  ----|
def search_concerto():
	print(" ==== Search Concert ==== ")
	c=0;
	nome_autor=input("> Type Concert Author Name: ")
	a=autor_check(nome_autor)
	if(a==False):
		cls()
		print(" No Match for Search: '%s' \n"%nome_autor)
		return
	else: 
		lookup_concerto(nome_autor)
	ans=True
	while ans:
		try:
			print("""
	1 - Search Another Concert
	2 - Back to Main Menu
			""")
			ans=input("> Please select an option: ")
			if ans=="1":
				cls()
				search_concerto()
			if ans=="2":
				cls()
				return			
		except KeyboardInterrupt:
			sys.exit()

##======== MENUS ========##
def user_menu():
	global user
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
		| 3.Search Album   |
		+------------------+
		| 4.Search Concert |
		+------------------+
		| 5.Make Review    |
		+------------------+
		| 6.Create Playlist|
		+------------------+
		| 7.View Playlists |
		+------------------+
		| 8.Delete Playlist|
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
				cls();
				search_music()
				
			elif ans=="2":
				cls();
				search_autor()
				
			elif ans=="3":
				cls();
				search_album()
			
			elif ans=="4":
				cls();
				search_concerto()
			
			elif ans=="5":
				cls();
				#Fazer Critica
				add_review()
			
			elif ans=="6":
				cls();
				#Cria Playlist
				if(add_playlist()==True):print("\n Playlist Successfully Inserted")
				#input("Press any key to exit")
			
			elif ans=="7":
				cls();
				#Ver Playlist
				list_playlist("todas",check_user(user))
				#input("Press any key to exit")
			
			elif ans=="7":
				cls();
				#Ver Playlist
				list_playlist("todas",check_user(user))
				#input("Press any key to exit")
			
			elif ans=="8":
				cls();
				#Delete Playlist
				#Verificar se Playlist existe
				nome_playlist=None
				c=0;
				while (check_playlist(nome_playlist)==False):
					if(c!=0):print(" ERROR, Type Playlist Name Again!")
					nome_playlist=input("> Type Playlist Name:")
					if(c>0):
						print("""
Playlist not present in Database
    1 - List Playlist's in Database
    2 - Try Again
    3 - Add New Playlist
						""")
						opt=input("> Please select an option: ")
						if opt=="1":
							cls()
							#Listar Autores
							list_playlist("user",check_user(user))
							search_music()
						elif opt=="2":
							cls();
							search_music()
						elif opt=="3":
							cls();
							#Check FO
							if(add_playlist()==True):
								print(" Playlist Insert Success")
								search_music()
						elif opt !="":
							cls()
							return
					c+=1
				delete_playlist(check_playlist(nome_playlist),check_user(user))
				#input("Press any key to exit")
				
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
	ans=True
	while ans:
		try:
			print ("""	_____________________________
	User: %s
		 
		+---------------+
		| 1.Add Music   |
		+---------------+
		| 2.Add Author  |
		+---------------+
		| 3.Add Composer|
		+---------------+
		| 4.Add ALbum   |
		+---------------+
		| 5.Add Concert |
		+---------------+
		| 0.Logout      |
		+---------------+
		| q.Exit        |
		+---------------+
	Version: %s
	_____________________________
			"""%(user,version))
			ans=input("> Please select an option: ")
			if ans=="1":
				cls()
				add_music();
			#Option -> add_music()
			elif ans=="2":
				cls();
				add_autor();
			#Option -> add_autor()
			elif ans=="3":
				cls();	
				add_composer();
			#Option -> add_composer()
			elif ans=="4":
				cls();	
				add_album();
			#Option -> add_album()
			elif ans=="5":
					cls();	
					add_concerto();
			#Option -> add_concerto()
			elif ans=="q":
				cls();
				print("\n Goodbye \n")
				sys.exit()
			elif ans=="0":
				print("\n Logging you out... Please wait")
				time.sleep(1.5) 
				cls()
				user=None
				int_main();
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
					cls()
					editor_menu()
				else :
					cls()
					user_menu()
			elif ans=="2":
				cls();
				register();
				#
				login();
				if user_lvl(user)=="editor":
					cls()
					editor_menu()
				else :
					cls()
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
user_menu()
#search_music()
#add_music()