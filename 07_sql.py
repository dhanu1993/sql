#update and delete records of population table from database

import sqlite3

with sqlite3.connect("new.db") as connection:
	cur = connection.cursor()
	cur.execute("UPDATE population SET population=9000000 WHERE city='New York City' ")
	cur.execute("DELETE from population WHERE City='Boston'")

	print("\nNEW DATA\n")
	cur.execute("SELECT * from population")
	rows=cur.fetchall()
	for r in rows:
		print(r)