from tkinter import * 
from tkinter import ttk
from DB import cursor,mydb
from main import mainpy
def displayscore(id):
	

	root = Tk()

	cursor.execute(f"select game,score from scores where id={id};")


	root.title('scores')


	score_tree = ttk.Treeview(root)
	score_tree['columns'] = ('Game',"Score")
	score_tree['show'] = 'headings'
	#formating
	score_tree.column("Game",width = 150,minwidth=150,anchor = CENTER)
	score_tree.column("Score",width = 150,minwidth=150,anchor = CENTER)

	#heading
	score_tree.heading("Game",text="Game",anchor=CENTER)
	score_tree.heading("Score",text="Score",anchor=CENTER)


	

	back_button = Button(root,text = "<--",command =lambda:back())

	def back():
		root.destroy()
		mainpy(id)

	i=0
	for ro in cursor:
		score_tree.insert('',i,text="",values=(ro[0],ro[1]))
		i = i+1

	sb = ttk.Scrollbar(root,orient="vertical")

	sb.configure(command = score_tree.yview)
	score_tree.configure(yscrollcommand = sb.set)
	sb.pack(fill = Y,side=RIGHT)
	score_tree.pack()
	back_button.pack()
	root.mainloop()