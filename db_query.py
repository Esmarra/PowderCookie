import pymysql

#==== DB Setings ====#
db_ip = "localhost" #"192.168.2.102"
db_user = "root"
db_pwd = ""
db_name = "basedados"
db_port = "" # 3306

# Find all Users
def get_user(user,password):
	db = None
	try:
		db = pymysql.connect(host=db_ip,user=db_user,password=db_pwd,db=db_name,port=db_port)
		cursor = db.cursor()
		sql = "SELECT username, password FROM utilizador"
		cursor.execute(sql)
		row = cursor.fetchone()
		while row is not None:
			# Validate Username and PWD here
			if(user==row[0] and password==row[1]):
				return True
			row = cursor.fetchone()
		cursor.close()

	except pymysql.err.OperationalError:
		print("db error, continue")
	finally:
		if db is not None:
			db.close()
			
	return False