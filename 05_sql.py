#display the records of employees table from database
import sqlite3

with sqlite3.connect("new.db") as conn:
	c=conn.cursor()
	for row in c.execute("SELECT * from employees"):
		print(row)


