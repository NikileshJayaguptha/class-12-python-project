import mysql.connector

mydb = mysql.connector.connect(host = "sql6.freemysqlhosting.net",user = "sql6478441",passwd = "BVpe4eB4NT", database = "sql6478441")

cursor = mydb.cursor()

#!create table users(username varchar(25) not null,password varchar(100),name varchar(100),id primary key);
#!create table scores(id int, FOREIGN KEY(id) REFERENCES users(id),score int, game varchar(255));
