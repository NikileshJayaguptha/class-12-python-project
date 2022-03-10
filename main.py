from tkinter import *
from turtle import back
from PIL import ImageTk,Image


from Chrome_Dinosaur.Chrome_Dinosaur import chromedinosaur
from Hand_Cricket.hand_cricket import handcricket
from Space_Invader.spaceinvader import spaceinvader

window = Tk()

#!load images
chromedinoimage = ImageTk.PhotoImage(Image.open("guiassets/chrome dinosaur.png"))
spaceinvaderimg = ImageTk.PhotoImage(Image.open("guiassets/space invader.png"))
handcricketimg = ImageTk.PhotoImage(Image.open("guiassets/Handcricket.png"))

text_list = ["Chrome Dinosaur","Space Invader","Handcricket"]

funclist = [chromedinosaur,spaceinvader,handcricket]
s = 0
imagelist = [chromedinoimage,spaceinvaderimg,handcricketimg]


l = len(imagelist)
imagelabel = Label(image=chromedinoimage)
imagelabel.grid(row = 0,column=0,columnspan=3)

#!Button
textlabel = Button(text = text_list[0], command=funclist[0])
textlabel.grid(row = 1,column=0,columnspan=3)


#!functions
def forward():
	global imagelabel
	global button_back
	global button_forward
	global textlabel
	global s
	global l
	s+=1
	if s<l and s>=0:
		
		
		imagelabel.grid_forget()
		imagelabel = Label(image=imagelist[s])

		textlabel.grid_forget()
		textlabel = Button(text=text_list[s], command=funclist[s])
		
		textlabel.grid(row = 1,column=0,columnspan=3)
		imagelabel.grid(row = 0,column=0,columnspan=3)
	

def backward():
	global imagelabel
	global button_back
	global button_forward
	global textlabel
	global s
	global l
	s-=1
	if s<l and s>=0:
		textlabel.grid_forget()
		textlabel = Button(text=text_list[s],command=funclist[s])
		
		imagelabel.grid_forget()
		imagelabel = Label(image=imagelist[s])
		
		textlabel.grid(row = 1,column=0,columnspan=3)
		imagelabel.grid(row = 0,column=0,columnspan=3)



#!Buttons
button_back = Button(window,text = "<<",command =lambda:backward())
button_exit = Button(window,text = "EXIT",command = window.quit)
button_forward = Button(window,text = ">>", command = lambda:forward())

button_back.grid(row = 2,column=0)
button_exit.grid(row = 2,column=1)
button_forward.grid(row=2,column=2)
#title of screen
window.title("blabla")
window.mainloop()