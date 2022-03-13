from tkinter import *
from DB import cursor,mydb
from main import mainpy
import bcrypt
import random

a =""
root = Tk()
root.geometry('500x200')
def login():
	login_button.destroy()
	signup_button.destroy()

	username_label = Label(root,text = "Username")
	username_label.place(relx = 0.15,rely = 0.25, anchor = CENTER)

	username_entry = Entry(root,font = ('Arial 16'))
	username_entry.place(relx = 0.5,rely = 0.25, anchor = CENTER )

	password_label = Label(root,text = "Password")
	password_label.place(relx = 0.15,rely = 0.5, anchor = CENTER)

	password_entry = Entry(root,font = ('Arial 16'))
	password_entry.place(relx = 0.5,rely = 0.5, anchor = CENTER )




	def submit():

		username = username_entry.get()

		cursor.execute(f"select password,id from users where username='{username}'")

		for i in cursor:
			hashedpwd = bytes(i[0],'utf-8')
			password = password_entry.get()
			password = bytes(password,'utf-8')
			if bcrypt.checkpw(password,hashedpwd):
				root.destroy()
				mainpy(i[1])



	submit_button = Button(root,text = "submit", command = submit)
	submit_button.place(relx = 0.5,rely = 0.75, anchor = CENTER)


def signup():
	username_label = Label(root,text = "Username")
	username_label.place(relx = 0.15,rely = 0.25, anchor = CENTER)

	username_entry = Entry(root,font = ('Arial 16'))
	username_entry.place(relx = 0.5,rely = 0.25, anchor = CENTER )

	password_label = Label(root,text = "Password")
	password_label.place(relx = 0.15,rely = 0.5, anchor = CENTER)

	password_entry = Entry(root,font = ('Arial 16'))
	password_entry.place(relx = 0.5,rely = 0.5, anchor = CENTER )

	name_entry = Entry(root,font = ('Arial 16'))
	name_entry.place(relx = 0.5,rely = 0.75, anchor = CENTER )

	name_label = Label(root,text = "Name")
	name_label.place(relx = 0.15,rely = 0.75, anchor = CENTER)


	
	def submit():
		salt = bcrypt.gensalt()

		# id for users
		cursor.execute("select id from users;")

		id1 = 0
		idlist = [0]

		for i in cursor:
			idlist.append(i[0])

		while id1 in idlist:
			id1 = random.randint(0,100000)




		username = username_entry.get()
		password = password_entry.get()
		#hash password
		password = bytes(password,"utf-8")
		password = bcrypt.hashpw(password,salt)
		password = password.decode()

		name = name_entry.get()
		
		cursor.execute(f'insert into users values("{username}","{password}","{name}","{id1}")')
		mydb.commit()

		username_label.destroy()
		username_entry.destroy()
		password_entry.destroy()
		password_label.destroy()
		name_entry.destroy()
		name_label.destroy()
		submit_button.destroy()
		login()

	submit_button = Button(root,text = "submit", command = submit)
	submit_button.place(relx = 0.5,rely = 0.925, anchor = CENTER)




login_button = Button(root,text="Login",command = login) 
signup_button = Button(root,text="Signup",command = signup) 

login_button.place(relx = 0.5,rely = 0.5, anchor = CENTER)
signup_button.place(relx = 0.5,rely = 0.25, anchor = CENTER)


root.mainloop()