from tkinter import *
from PIL import ImageTk,Image
from graph import agraph

def mainpy(id1):
	global c
	global s
	global l
	global imagelabel
	global textlabel
	global game

	
	from Chrome_Dinosaur.Chrome_Dinosaur import chromedinosaur
	from Hand_Cricket.hand_cricket import handcricket
	from Space_Invader.spaceinvader import spaceinvader
	from display_score import displayscore


	window = Tk()


	#!load images
	chromedinoimage = ImageTk.PhotoImage(Image.open("guiassets/chrome dinosaur.png"))
	spaceinvaderimg = ImageTk.PhotoImage(Image.open("guiassets/space invader.png"))
	handcricketimg = ImageTk.PhotoImage(Image.open("guiassets/Handcricket.png"))

	text_list = ["Chrome Dinosaur","Space Invader","Handcricket"]
	db_list = ["chromedinosaur","spaceinvader","handcricket"]

	game = db_list[0]
	funclist = [chromedinosaur,spaceinvader,handcricket]

	s = 0

	imagelist = [chromedinoimage,spaceinvaderimg,handcricketimg]


	l = len(imagelist)
	imagelabel = Label(image=chromedinoimage)
	imagelabel.grid(row = 1,column=0,columnspan=3)

	#!Button
	textlabel = Button(text = text_list[0], command=lambda:funclist[0](id1))
	textlabel.grid(row = 3,column=0,columnspan=3)


	#!functions
	def forward():
		global imagelabel
		global button_back
		global button_forward
		global textlabel
		global game
		global s
		global l
		s+=1
		if s<l and s>=0:
			
			
			imagelabel.grid_forget()
			imagelabel = Label(image=imagelist[s])

			textlabel.grid_forget()
			textlabel = Button(text=text_list[s], command= lambda:funclist[s](id1))

			game = db_list[s]

			
			textlabel.grid(row = 3,column=0,columnspan=3)
			imagelabel.grid(row = 1,column=0,columnspan=3)
		

	def backward():
		global imagelabel
		global button_back
		global button_forward
		global textlabel
		global game
		global s
		global l
		s-=1
		if s<l and s>=0:
			textlabel.grid_forget()
			textlabel = Button(text=text_list[s],command=funclist[s])
			
			imagelabel.grid_forget()
			imagelabel = Label(image=imagelist[s])

			game = db_list[s]
			
			textlabel.grid(row = 3,column=0,columnspan=3)
			imagelabel.grid(row = 1,column=0,columnspan=3)



	def scores():
		window.destroy()
		displayscore(id1)

	#!Buttons
	button_back = Button(window,text = "<<",command =lambda:backward())
	button_exit = Button(window,text = "EXIT",command = window.quit)
	button_forward = Button(window,text = ">>", command = lambda:forward())
	score = Button(window,text = "SCORES",command =lambda:scores())
	button_graph = Button(window,text = "GRAPH", command = lambda:agraph(game))

	
	button_back.grid(row = 3,column=0)
	score.grid(row = 4,column=0)
	button_graph.grid(row = 4 ,column=1)
	button_exit.grid(row = 4,column=2)
	button_forward.grid(row=3,column=2)
	#title of screen
	window.title("Games")
	
	window.mainloop()
