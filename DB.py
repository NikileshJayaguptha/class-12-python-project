import mysql.connector

mydb = mysql.connector.connect(host = "sql6.freemysqlhosting.net",user = "sql6478441",passwd = "BVpe4eB4NT", database = "sql6478441")

cursor = mydb.cursor()

cursor.execute("select password from users where username = 'abc';")

for i in cursor:
	print(i)