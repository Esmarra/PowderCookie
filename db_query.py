import pymysql
import time
from time import localtime, strftime

#==== DB Setings ====#
db_ip = "localhost" #"192.168.2.102"
db_user = "root"
db_pwd = ""
db_name = "basedados"
db_port = "" # 3306

def db_fetch(query):
	db = pymysql.connect(host=db_ip,user=db_user,password=db_pwd,db=db_name,port=db_port)
	cursor = db.cursor()
	cursor.execute(query)
	return cursor.fetchone()

# Get User From DB and compare with program login
def get_user(user,password,type):
	value = False
	db = None
	try:
		db = pymysql.connect(host=db_ip,user=db_user,password=db_pwd,db=db_name,port=db_port)
		cursor = db.cursor()
		sql = "SELECT username, password FROM utilizador"
		cursor.execute(sql)
		row = cursor.fetchone()
		while row is not None:
			#Type L (Login) User and PWD Validaion
			if type=="l":
				if(user==row[0] and password==row[1]):
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
		sql = "INSERT INTO utilizador(name,username,password,user_level,data_de_registo\
				)VALUES ('%s','%s','%s','%s','%s')"%(name,user,password,edit,date)
		cursor.execute(sql)
		db.commit()
		value = True
	except pymysql.err.OperationalError:
		print("db error, continue")
	finally:
		if db is not None:
			db.close()
	return value
	
#Get Usr_lvl
def user_lvl(user):
	db = None
	db = pymysql.connect(host=db_ip,user=db_user,password=db_pwd,db=db_name,port=db_port)
	cursor = db.cursor()
	sql="SELECT user_level FROM utilizador WHERE username = '%s'"%user
	cursor.execute(sql)
	result = cursor.fetchone()
	return(result[0])

#Check Author
def autor_check(autor):
	db = None
	db = pymysql.connect(host=db_ip,user=db_user,password=db_pwd,db=db_name,port=db_port)
	cursor = db.cursor()
	sql="SELECT autor_id FROM autor WHERE nome = '%s'"%autor
	cursor.execute(sql)
	result = cursor.fetchone()
	return(result[0])