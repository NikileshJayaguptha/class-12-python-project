import mysql.connector

mydb = mysql.connector.connect(host = "sql6.freemysqlhosting.net",user = "sql6478441",passwd = "BVpe4eB4NT", database = "sql6478441")

cursor = mydb.cursor()

cursor.execute("select * from test;")

for i in cursor:
	print(i[0])