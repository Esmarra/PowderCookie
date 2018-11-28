# Program Name :	Music_for_all database querys
# Base Language:	MixedEnglish
# Created by   :	Esmarra
# Creation Date:	20/11/2018
# Rework date entries:
# Program Objectives:
# Observations:
# Special Thanks:
version ="Alfa0.5"

# ==== Imports ===== #
import pymysql
import time
from time import localtime, strftime
import hashlib

#==== DB Setings ====#
db_ip = "localhost" #"192.168.2.102"
db_user = "root"
db_pwd = ""
db_name = "basedados"
db_port = "" # 3306


##======== TABELA UTILIZADOR ========##
#|----  Get User From DB ----| compare with program login
def get_user(user,password,type):
	hashed_pwd=hashlib.sha512(password.encode('utf-8')).hexdigest()
	value = False
	db = None
	try:
		db = pymysql.connect(host=db_ip,user=db_user,password=db_pwd,db=db_name,port=db_port)
		cursor = db.cursor()
		sql = "SELECT username, e_pwd FROM utilizador"
		cursor.execute(sql)
		row = cursor.fetchone()
		while row is not None:
			#Type L (Login) User and PWD
			if type=="l":
				if(user==row[0] and hashed_pwd==row[1].decode('utf-8')):
					value = True
			#Type R (Register) User only Validaion
			if type =="r":
				if(user==row[0]):
					value = True
			row = cursor.fetchone()
		cursor.close()

	except pymysql.err.OperationalError:
		print("db error, continue")
	finally:
		if db is not None:
			db.close()
			
	return value

#|----  Register User ----| checks if username is duplicate
def register_user(name,user,password,edit):
	#Check for Duplicate Username
	if get_user(user,password,"r") == True:
		#Username Taken
		return False
	date=time.strftime("%Y-%m-%d", time.localtime())

	try:
		db = pymysql.connect(host=db_ip,user=db_user,password=db_pwd,db=db_name,port=db_port)
		cursor = db.cursor()
		sql = "INSERT INTO utilizador(name,username,e_pwd,user_level,data_de_registo\
				)VALUES ('%s','%s','%s','%s','%s')"%(name,user,hashlib.sha512(password.encode('utf-8')).hexdigest(),edit,date)
		cursor.execute(sql)
		db.commit()
		value = True
	except pymysql.err.OperationalError:
		print("db error, continue")
	finally:
		if db is not None:
			db.close()
	return value

#|----  Get Usr_lvl ----| admin or editor
def user_lvl(user):
	db = None
	db = pymysql.connect(host=db_ip,user=db_user,password=db_pwd,db=db_name,port=db_port)
	cursor = db.cursor()
	sql="SELECT user_level FROM utilizador WHERE username = '%s'"%user
	cursor.execute(sql)
	result = cursor.fetchone()
	return(result[0])

#|----  Check User ----| returns user_id(int)
def check_user(user):
	db = None
	db = pymysql.connect(host=db_ip,user=db_user,password=db_pwd,db=db_name,port=db_port)
	cursor = db.cursor()
	sql = "SELECT user_id FROM utilizador WHERE username='%s'"%user
	cursor.execute(sql)
	result = cursor.fetchone()
	if(result!=None):
		return(result[0])
	else:
		return(False)



##======== TABELA AUTOR ========##
#|----  Check Author ----| returns autor_id(int)
def autor_check(autor):
	db = None
	db = pymysql.connect(host=db_ip,user=db_user,password=db_pwd,db=db_name,port=db_port)
	cursor = db.cursor()
	sql="SELECT autor_id FROM autor WHERE nome = '%s'"%autor
	cursor.execute(sql)
	result = cursor.fetchone()
	if(result!=None):
		return(result[0])
	else:
		return(False)

#|---- Insert Author ----|
def insert_autor(a_nome,a_historia):
	try:
		db = pymysql.connect(host=db_ip,user=db_user,password=db_pwd,db=db_name,port=db_port)
		cursor = db.cursor()
		sql = "INSERT INTO autor(nome,historia)VALUES ('%s','%s')"%(a_nome,a_historia)
		cursor.execute(sql)
		db.commit()
		value = True
	except pymysql.err.OperationalError:
		print("db error, continue")
		value = False
	finally:
		if db is not None:
			db.close()
	return value

#|---- List Author ----| Displays All Authors / Returns Array with a.id
def list_autor():
	cnt=0
	try:
		db = pymysql.connect(host=db_ip,user=db_user,password=db_pwd,db=db_name,port=db_port)
		cursor = db.cursor()
		sql = "SELECT nome,autor_id FROM autor ORDER BY nome"
		#Create Music_ID Array Map
		id_map=[]
		cursor.execute(sql)
		row = cursor.fetchone()
		while row is not None:
			cnt += 1
			print(" %d - %s"%(cnt,row[0]))
			#Append Each Result to Array
			id_map.append(row[1])
			row = cursor.fetchone()
		cursor.close()

	except pymysql.err.OperationalError:
		print("db error, continue")
	finally:
		if db is not None:
			db.close()
	return id_map
arr=list_autor()
print(arr)

#|---- Lookup Author ----| é o list autor? 

#|---- Update History ----|
def update_history(autor_id,historia):
	try:
		db = pymysql.connect(host=db_ip,user=db_user,password=db_pwd,db=db_name,port=db_port)
		cursor = db.cursor()
		sql = "UPDATE autor SET historia ='%s' WHERE autor_id='%s'"%(historia,autor_id)
		cursor.execute(sql)
		db.commit()
		value = True
	except pymysql.err.OperationalError:
		print("db error, continue")
		value = False
	finally:
		if db is not None:
			db.close()
	return value
#update_history("4","Continuo a achar que é mas ok")



##======== TABELA COMPOSITOR ========## 
#|---- Check Composer ----|
def composer_check(composer):
	db = None
	db = pymysql.connect(host=db_ip,user=db_user,password=db_pwd,db=db_name,port=db_port)
	cursor = db.cursor()
	sql="SELECT compositor_id FROM compositor WHERE nome = '%s'"%composer
	cursor.execute(sql)
	result = cursor.fetchone()
	if(result!=None):
		return(result[0])
	else:
		return(False)

#|---- Insert Composer ----|
def insert_comp(c_nome,c_genero,c_birthdate):
	try:
		db = pymysql.connect(host=db_ip,user=db_user,password=db_pwd,db=db_name,port=db_port)
		cursor = db.cursor()
		sql = "INSERT INTO compositor(nome,genero,data_de_nascimento)VALUES ('%s','%s','%s')"%(c_nome,c_genero,c_birthdate)
		cursor.execute(sql)
		db.commit()
		value = True
	except pymysql.err.OperationalError:
		print("db error, continue")
		value = False
	finally:
		if db is not None:
			db.close()
	return value

#|---- List Composer ----|
def list_composer():
	cnt=0
	try:
		db = pymysql.connect(host=db_ip,user=db_user,password=db_pwd,db=db_name,port=db_port)
		cursor = db.cursor()
		sql = "SELECT nome FROM compositor ORDER BY nome"
		cursor.execute(sql)
		row = cursor.fetchone()
		while row is not None:
			cnt += 1
			print(" %d - %s "%(cnt,row[0]))
			row = cursor.fetchone()
		cursor.close()

	except pymysql.err.OperationalError:
		print("db error, continue")
	finally:
		if db is not None:
			db.close()
	return
#list_composer()



##======== TABELA MUSICA ========##
#|---- Insert Music ----| (flag diz se faz query com album ou sem)
def insert_music(m_nome,m_genero,letra,m_time,c_id,a_id,autor_id,flag):
	try:
		db = pymysql.connect(host=db_ip,user=db_user,password=db_pwd,db=db_name,port=db_port)
		cursor = db.cursor()
		if(flag=='a'): # Tem Album Id 
			sql = "INSERT INTO musica(nome,genero,letra,tempo_da_musica,compositor_compositor_id \
				,album_album_id,autor_autor_id)VALUES ('%s','%s','%s','%s','%s','%s','%s')"%(m_nome,m_genero,letra,m_time,c_id,a_id,autor_id)
		else:
			#Query Sem Album ID (nao estava a dar para enviar "NULL" no python) Yey If it works it aint stupid ;)
			sql = "INSERT INTO musica(nome,genero,letra,tempo_da_musica,compositor_compositor_id \
				,autor_autor_id)VALUES ('%s','%s','%s','%s','%s','%s')"%(m_nome,m_genero,letra,m_time,c_id,autor_id)
			
		cursor.execute(sql)
		db.commit()
		value = True
	except pymysql.err.OperationalError:
		print("db error, continue")
		value = False
	finally:
		if db is not None:
			db.close()
	return value
	
#|---- Check Music ----| given name, retuns music_id(int)
def music_check(nome_music,autor_id):
	db = None
	db = pymysql.connect(host=db_ip,user=db_user,password=db_pwd,db=db_name,port=db_port)
	cursor = db.cursor()
	sql="SELECT musica_id FROM musica WHERE nome = '%s' and autor_autor_id='%s'"%(nome_music,autor_id)
	cursor.execute(sql)
	result = cursor.fetchone()
	if(result!=None):
		return(result[0])
	else:
		return(False)
#print(music_check("TNT","1"))

#|---- List Music ----| Displays All Music / Returns Array with m.id
def list_music():
	cnt=0
	try:
		db = pymysql.connect(host=db_ip,user=db_user,password=db_pwd,db=db_name,port=db_port)
		cursor = db.cursor()
		sql = """SELECT m.nome,a.nome,c.nome,m.genero,m.musica_id
					FROM musica m,autor a,compositor c
					WHERE m.autor_autor_id = a.autor_id
					AND m.compositor_compositor_id = c.compositor_id
					ORDER BY m.nome
				"""	
		print("|ID|    Nome    |   Autor  |  Compositor |  Genero  |\n")
		#Create Music_ID Array Map
		id_map=[]
		cursor.execute(sql)
		row = cursor.fetchone()
		while row is not None:
			cnt += 1
			print(" %d  %s   %s   %s   '%s'"%(cnt,row[0],row[1],row[2],row[3]))
			#Append Each Result to Array
			id_map.append(row[4])
			row = cursor.fetchone()
		cursor.close()

	except pymysql.err.OperationalError:
		print("db error, continue")
	finally:
		if db is not None:
			db.close()
	return id_map
#ar=list_music()
#print(ar)

#|---- Update Letra ----|
#def update_letra():


#|---- Lookup Music ----| Working
def lookup_music(nome_musica,nome_autor):
	cnt=0
	try:
		db = pymysql.connect(host=db_ip,user=db_user,password=db_pwd,db=db_name,port=db_port)
		cursor = db.cursor()
		sql = """SELECT m.nome,a.nome,c.nome,m.genero,m.musica_id
					FROM musica m,autor a,compositor c
					WHERE m.autor_autor_id = a.autor_id
					AND m.compositor_compositor_id = c.compositor_id
					AND m.nome='%s'
					AND a.nome='%s'
				"""%(nome_musica,nome_autor)
		print("|ID|    Nome    |   Autor  |  Compositor |  Genero  |\n")
		#Create Music_ID Array Map
		id_map=[]
		cursor.execute(sql)
		row = cursor.fetchone()
		while row is not None:
			cnt += 1
			print(" %d  %s   %s   %s   '%s'"%(cnt,row[0],row[1],row[2],row[3]))
			#Append Each Result to Array
			id_map.append(row[4])
			row = cursor.fetchone()
		cursor.close()

	except pymysql.err.OperationalError:
		print("db error, continue")
	finally:
		if db is not None:
			db.close()
	return id_map
#ar=lookup_music("Amar Pelos Dois","Salvador Sobral")
#print(ar)

#|---- Update Music Album ----| given music id,autor_id Join Music to album id
def update_music_album(music_id,autor_id,album_id):
	try:
		db = pymysql.connect(host=db_ip,user=db_user,password=db_pwd,db=db_name,port=db_port)
		cursor = db.cursor()
		sql = "UPDATE musica SET album_album_id ='%s' WHERE musica_id='%s' \
				AND autor_autor_id='%s' "%(album_id,music_id,autor_id)
		cursor.execute(sql)
		db.commit()
		value = True
	except pymysql.err.OperationalError:
		print("db error, continue")
		value = False
	finally:
		if db is not None:
			db.close()
	return value
#update_music_album("20","2","3")



##======== TABELA ALBUM ========##
#|---- Check Album ----| given name, retuns album_id(int)
def album_check(nome_album):
	db = None
	db = pymysql.connect(host=db_ip,user=db_user,password=db_pwd,db=db_name,port=db_port)
	cursor = db.cursor()
	sql="SELECT album_id FROM album WHERE nome = '%s'"%nome_album
	cursor.execute(sql)
	result = cursor.fetchone()
	if(result!=None):
		return(result[0])
	else:
		return(False)
#print(album_check("the cherry on my cake"))

#|---- Album Verify ----| #fazer codigo aqui BUGGADO MANEL WTF
def album_compare(nome_album, album_id):
	db = None
	db = pymysql.connect(host=db_ip,user=db_user,password=db_pwd,db=db_name,port=db_port)
	cursor = db.cursor()
	sql="SELECT nome FROM album WHERE nome = '%s'"%nome_album
	sq="SELECT nome FROM autor WHERE autor_id = '%s'"%album_id
	cursor.execute(sql)
	result = cursor.fetchone()
	if(result!=None):
		return(result[0])
	else:
		return(False)

#|---- Insert Album ----|
def insert_album(a_nome, a_data, a_editora, a_ano, a_id):
	try:
		db = pymysql.connect(host=db_ip,user=db_user,password=db_pwd,db=db_name,port=db_port)
		cursor = db.cursor()
		sql = "INSERT INTO album(nome, data, editora, \
				ano, autor_autor_id)VALUES ('%s','%s','%s','%s','%s')"%(a_nome, a_data, a_editora, a_ano, a_id)
		cursor.execute(sql)
		db.commit()
		value = True
	except pymysql.err.OperationalError:
		print("db error, continue")
		value = False
	finally:
		if db is not None:
			db.close()
	return value
#insert_album("Curtian Call","2018-10-01","virgin","2018","6")

#|---- List album ----|
def list_album():
	cnt=0
	try:
		db = pymysql.connect(host=db_ip,user=db_user,password=db_pwd,db=db_name,port=db_port)
		cursor = db.cursor()
		sql = "SELECT nome,album_id FROM album ORDER BY nome"
		#Create Album_ID Array Map
		id_map=[]
		cursor.execute(sql)
		row = cursor.fetchone()
		while row is not None:
			cnt += 1
			print(" %d - %s"%(cnt,row[0]))
			#Append Each Result to Array
			id_map.append(row[1])
			row = cursor.fetchone()
		cursor.close()

	except pymysql.err.OperationalError:
		print("db error, continue")
	finally:
		if db is not None:
			db.close()
	return id_map
#ar=list_album()
#print(ar)



##======== TABELA ALBUM_REVIEW ========##
#|----  Insert review ----|
def insert_review(r_review, r_rating,alb_id,user_id):
	date=time.strftime("%Y-%m-%d", time.localtime())
	try:
		db = pymysql.connect(host=db_ip,user=db_user,password=db_pwd,db=db_name,port=db_port)
		cursor = db.cursor()
		sql = "INSERT INTO album_review(review, rating,data,album_album_id,utilizador_user_id)VALUES ('%s','%d','%s','%s','%s')"%(r_review,r_rating,date,alb_id,user_id)
		cursor.execute(sql)
		db.commit()
		value = True
	except pymysql.err.OperationalError:
		print("db error, continue")
		value = False
	finally:
		if db is not None:
			db.close()
	return value
#insert_review("Gostei",int("5"),"2","21") # Change Album_id if you test

#|----  Update Review ----|
def update_review(r_id,nova_review,r_rating,alb_id,user_id):
	date=time.strftime("%Y-%m-%d", time.localtime())
	try:
		db = pymysql.connect(host=db_ip,user=db_user,password=db_pwd,db=db_name,port=db_port)
		cursor = db.cursor()
		sql = "UPDATE album_review SET review ='%s', rating='%d',data='%s',album_album_id='%s',\
			utilizador_user_id='%s' WHERE review_id='%s'"%(nova_review,r_rating,date,alb_id,user_id,r_id)
		cursor.execute(sql)
		db.commit()
		value = True
	except pymysql.err.OperationalError:
		print("db error, continue")
		value = False
	finally:
		if db is not None:
			db.close()
	return value
#update_review("1","Ouvi Outra vez é mais ou menos afinal",int("3"),"1","20")



##======== TABELA PLAYLIST ========##
#|---- Check playlist ----| [USELESS]
def playlist_check(nome_playlist):
	db = None
	db = pymysql.connect(host=db_ip,user=db_user,password=db_pwd,db=db_name,port=db_port)
	cursor = db.cursor()
	sql="SELECT playlist_id FROM playlist WHERE nome = '%s'"%nome_playlist
	cursor.execute(sql)
	result = cursor.fetchone()
	if(result!=None):
		return(result[0])
	else:
		return(False)

#|---- Insert playlist ----|
def insert_playlist(pl_nome, pl_privacidade, pl_userid):
	date=time.strftime("%Y-%m-%d", time.localtime())
	try:
		db = pymysql.connect(host=db_ip,user=db_user,password=db_pwd,db=db_name,port=db_port)
		cursor = db.cursor()
		sql = "INSERT INTO playlist(nome,data_de_criacao, privacidade,\
				utilizador_user_id)VALUES ('%s','%s','%s','%s')"%(pl_nome,date,pl_privacidade, pl_userid)
		cursor.execute(sql)
		db.commit()
		value = True
	except pymysql.err.OperationalError:
		print("db error, continue")
		value = False
	finally:
		if db is not None:
			db.close()
	return value
#insert_playlist("musicas_fofas","1","20")

#|---- List playlist ----|
def list_playlist(type,uid):
	cnt=0
	try:
		db = pymysql.connect(host=db_ip,user=db_user,password=db_pwd,db=db_name,port=db_port)
		cursor = db.cursor()
		#Display user only Playlists
		if(type=="user"): 
			sql = "SELECT nome,data_de_criacao,privacidade,playlist_id FROM playlist WHERE  utilizador_user_id='%s' \
					ORDER BY data_de_criacao" %(uid)
			print("|ID|    Nome    |    Data Criaçao |  Publica  |\n")
		#Disp todas as playlists publicas
		if(type=="publicas"): 
			sql = "SELECT p.nome,p.data_de_criacao,u.username,p.playlist_id FROM playlist p,utilizador u \
				WHERE privacidade=0 AND (u.user_id=utilizador_user_id)"
			print("|ID|    Nome    |    Data Criaçao |  Criador  |\n")
		#Create Playlist_ID Array Map
		id_map=[]
		cursor.execute(sql)
		row = cursor.fetchone()
		while row is not None:
			cnt += 1
			if(type=="user"): 
				if(row[2]==0):val="Sim" #0-> nao é privada entao é publica
				else: val="Nao"
				print(" %d  %s     %s        %s"%(cnt,row[0],row[1],val))
			if(type=="publicas"): 
				print(" %d  %s     %s        %s"%(cnt,row[0],row[1],row[2]))
				
			id_map.append(row[3])
			row = cursor.fetchone()
		cursor.close()

	except pymysql.err.OperationalError:
		print("db error, continue")
	finally:
		if db is not None:
			db.close()
	return
#arr=list_playlist("user","20")
#arr=list_playlist("publicas","20")
#print(arr)

#|---- Delete Playlist ----| (pode nao estar 100% correcta)
def delete_playlist(pl_id,uid):
	try:
		db = pymysql.connect(host=db_ip,user=db_user,password=db_pwd,db=db_name,port=db_port)
		cursor = db.cursor()
		sql = "DELETE FROM playlist WHERE playlist_id='%s' and utilizador_user_id='%s'"%(pl_id,uid)
		cursor.execute(sql)
		db.commit()
		value = True
	except pymysql.err.OperationalError:
		print("db error, continue")
		value = False
	finally:
		if db is not None:
			db.close()
	return value
#delete_playlist("9","19")



##======== TABELA PLAYLIST_MUSICA ========##
def insert_playlist_music(pl_id,music_id):
	try:
		db = pymysql.connect(host=db_ip,user=db_user,password=db_pwd,db=db_name,port=db_port)
		cursor = db.cursor()
		sql = "INSERT INTO playlist_musica(playlist_playlist_id,musica_musica_id) \
			VALUES ('%s','%s')"%(pl_id,music_id)
		cursor.execute(sql)
		db.commit()
		value = True
	except pymysql.err.OperationalError:
		print("db error, continue")
		value = False
	finally:
		if db is not None:
			db.close()
	return value
#insert_playlist_music("6","13")



##======== TABELA MEMBROS ========## 
# Check Membro BUGGED
def membro_check(nome_membro):
	db = None
	db = pymysql.connect(host=db_ip,user=db_user,password=db_pwd,db=db_name,port=db_port)
	cursor = db.cursor()
	sql="SELECT membro_id FROM membros WHERE nome = '%s'"%nome_membro
	cursor.execute(sql)
	result = cursor.fetchone()
	if(result!=None):
		return(result[0])
	else:
		return(False)

#|---- Insert Membro ----|
def insert_membro(m_nome, m_historia, m_data_de_nascimento, m_autor_autor_id):
	try:
		db = pymysql.connect(host=db_ip,user=db_user,password=db_pwd,db=db_name,port=db_port)
		cursor = db.cursor()
		sql = "INSERT INTO membros(nome, historia, data_de_nascimento\
				,autor_autor_id)VALUES ('%s','%s','%s','%s')"%(m_nome, m_historia, m_data_de_nascimento, m_autor_autor_id)
		cursor.execute(sql)
		db.commit()
		value = True
	except pymysql.err.OperationalError:
		print("db error, continue")
		value = False
	finally:
		if db is not None:
			db.close()
	return value
#insert_membro("pessoa","uma vez comeu alface","1993-06-12","4")



##======== TABELA CONCERTOS ========##
#|----  Insert Concerto ----|
def insert_concerto(c_sitio, c_data, autor_concerto):
	try:
		db = pymysql.connect(host=db_ip,user=db_user,password=db_pwd,db=db_name,port=db_port)
		cursor = db.cursor()
		sql = "INSERT INTO concertos(sitio, data,\
				autor_autor_id)VALUES ('%s','%s','%s')"%(c_sitio, c_data, autor_concerto)
		cursor.execute(sql)
		db.commit()
		value = True
	except pymysql.err.OperationalError:
		print("db error, continue")
		value = False
	finally:
		if db is not None:
			db.close()
	return value
#insert_concerto("Alive","2018-10-12","7")

#|---- Update concerto ----| given consert id, date,sitio,autor_id
def update_concerto(con_id,con_data,sitio,autor_id):
	try:
		db = pymysql.connect(host=db_ip,user=db_user,password=db_pwd,db=db_name,port=db_port)
		cursor = db.cursor()
		sql = "UPDATE concertos SET data ='%s', sitio='%s',autor_autor_id='%s' WHERE concerto_id='%s'"%(con_data,sitio,autor_id,con_id)
		cursor.execute(sql)
		db.commit()
		value = True
	except pymysql.err.OperationalError:
		print("db error, continue")
		value = False
	finally:
		if db is not None:
			db.close()
	return value
#update_concerto("1","2018-10-12","Colizeu","2")