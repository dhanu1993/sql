import	sqlite3

with sqlite3.connect("newnum.db") as connection:
	c=connection.cursor()
	prompt	=	"""
	Select the operation that you want to perform [1-5]:
	1. average
	2. Max
	3. Min
	4. Sum
	5. Exit
	"""
	while True:
		x=int(input(prompt))
		if x in set([1,2,3,4]):
			operation={1:"AVG",2:"MAX",3:"MIN",4:"SUM"}
			c.execute("SELECT {}(num) from numbers".format(operation[x]))
			print(operation[x]+":", c.fetchone())
		elif x == 5:
			print("Exit")
			break