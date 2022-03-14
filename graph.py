def agraph(game):
	import matplotlib.pyplot as plot
	from DB import cursor,mydb
	a = []
	j = 0
	b = []
	cursor.execute(f"select score from scores where game='{game}'")
	for i in cursor:
		a.append(i[0])
		b.append(j)
		j+=1


	plot.plot(b,a)
	plot.show()

