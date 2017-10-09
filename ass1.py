import sqlite3

######   assignment 1   ###########

with sqlite3.connect("cars.db") as connection:
	cursor=connection.cursor()
	cursor.execute("INSERT INTO inventory VALUES('Ford', 'Focus', 10)")
	cursor.execute("INSERT INTO inventory VALUES('Honda', 'Civic', 11)")
	cursor.execute("INSERT INTO inventory VALUES('Ford', 'Ranger', 12)")
	cursor.execute("INSERT INTO inventory VALUES('Honda', 'Accord', 13)")
	cursor.execute("INSERT INTO inventory VALUES('Ford', 'Avenger', 14)")



#######   assignment 2   ###########

# with sqlite3.connect("cars.db") as connection:
# 	cursor=connection.cursor()
# 	cursor.execute("UPDATE inventory SET quntity=20 where model='Accord'")
# 	cursor.execute("UPDATE inventory SET quntity=30 where model='Avenger'")

# 	for row in cursor.execute("SELECT * FROM inventory"):
# 		print(row)


########   assignment 3   #######
# with sqlite3.connect("cars.db") as connection:
# 	cursor=connection.cursor()
# 	for row in cursor.execute("SELECT * FROM inventory WHERE vehical='Ford'"):
# 		print(row)


######   output checking   #####
with sqlite3.connect("cars.db") as connection:
	cursor=connection.cursor()
	for row in cursor.execute("SELECT * FROM inventory"):
 		print(row)