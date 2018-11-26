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


# Get User From DB and compare with program login
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

# Register User in DB also checks if username is duplicate
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
	
# Get Usr_lvl
def user_lvl(user):
	db = None
	db = pymysql.connect(host=db_ip,user=db_user,password=db_pwd,db=db_name,port=db_port)
	cursor = db.cursor()
	sql="SELECT user_level FROM utilizador WHERE username = '%s'"%user
	cursor.execute(sql)
	result = cursor.fetchone()
	return(result[0])

# Check Author
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

#Insert Author
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

#List Author
def list_autor():
	cnt=0
	try:
		db = pymysql.connect(host=db_ip,user=db_user,password=db_pwd,db=db_name,port=db_port)
		cursor = db.cursor()
		sql = "SELECT nome FROM autor ORDER BY nome"
		cursor.execute(sql)
		row = cursor.fetchone()
		while row is not None:
			cnt += 1
			print(" %d - %s"%(cnt,row[0]))
			row = cursor.fetchone()
		cursor.close()

	except pymysql.err.OperationalError:
		print("db error, continue")
	finally:
		if db is not None:
			db.close()
	return

# Check Composer
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

# Insert Composer
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

# List Composer
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

# Insert Music (flag diz se faz query com album ou sem)
def insert_music(m_nome,m_genero,letra,m_time,c_id,a_id,autor_id,flag):
	try:
		db = pymysql.connect(host=db_ip,user=db_user,password=db_pwd,db=db_name,port=db_port)
		cursor = db.cursor()
		if(flag=='a'): # Tem Album Id 
			sql = "INSERT INTO musica(nome,genero,letra,tempo_da_musica,compositor_compositor_id,album_album_id,autor_autor_id)VALUES ('%s','%s','%s','%s','%s','%s','%s')"%(m_nome,m_genero,letra,m_time,c_id,a_id,autor_id)
		else:
			#Query Sem Album ID (nao estava a dar para enviar "NULL") Yey If it works it aint stupid ;)
			sql = "INSERT INTO musica(nome,genero,letra,tempo_da_musica,compositor_compositor_id,autor_autor_id)VALUES ('%s','%s','%s','%s','%s','%s')"%(m_nome,m_genero,letra,m_time,c_id,autor_id)
			
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



#______ MATEUS ______#

# Insert Review (Mateus)
def insert_review(review, rating):
	try:
		db = pymysql.connect(host=db_ip,user=db_user,password=db_pwd,db=db_name,port=db_port)
		cursor = db.cursor()
		sql = "INSERT INTO album_review(review, rating)VALUES ('%s','%d')"%(review, rating)
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
	
# Check Album (Mateus)
def album_check(n_album):
	db = None
	db = pymysql.connect(host=db_ip,user=db_user,password=db_pwd,db=db_name,port=db_port)
	cursor = db.cursor()
	sql="SELECT autor_id FROM autor WHERE nome = '%s'"%n_album
	cursor.execute(sql)
	result = cursor.fetchone()
	if(result!=None):
		return(result[0])
	else:
		return(False)

# Insert Album (Mateus)
def insert_album(a_nome,a_data,a_editora,a_ano,a_id):
	try:
		db = pymysql.connect(host=db_ip,user=db_user,password=db_pwd,db=db_name,port=db_port)
		cursor = db.cursor()
		sql = "INSERT INTO album(nome, data, editora, \
				ano,autor_id)VALUES ('%s','%s','%s','%s','%s')"%(a_nome, a_data, a_editora,a_ano,a_id)
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