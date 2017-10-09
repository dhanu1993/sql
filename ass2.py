import sqlite3


#######   assignment 1   ###########

# with sqlite3.connect("cars.db") as connection:
# 	cursor=connection.cursor()
# 	cursor.execute("CREATE TABLE orders(make TEXT, model TEXT,order_date DATE)")
# 	orders = [
# 		('Ford', 'Focus', '2014-01-22'),
# 		('Ford', 'Focus', '2014-01-23'),
# 		('Ford', 'Focus', '2014-01-24'),
#         ('Honda', 'Civic', '2014-01-25'),
#         ('Honda', 'Civic', '2014-01-26'),
#         ('Honda', 'Civic', '2014-01-27'),
# 		('Ford', 'Ranger', '2014-01-28'),		
# 		('Ford', 'Ranger', '2014-01-22'),
# 		('Ford', 'Ranger', '2014-01-23'),
# 		('Honda', 'Accord', '2014-01-24'),
# 		('Honda', 'Accord', '2014-01-25'),
# 		('Honda', 'Accord', '2014-01-26'),
# 		('Ford', 'Avenger', '2014-01-27'),
# 		('Ford', 'Avenger', '2014-01-28'),
# 		('Ford', 'Avenger', '2014-01-22')
# 	]
# 	cursor.executemany("INSERT INTO orders VALUES(?,?,?)", orders)
# 	cursor.execute("SELECT * FROM orders ORDER BY order_date ASC")
# 	rows=cursor.fetchall()
# 	for row in rows:
# 		print(row)


########   assignment 2   #######
# with sqlite3.connect("cars.db") as connection:
# 	cursor=connection.cursor()
# 	cursor.execute("SELECT orders.make,orders.model,inventory.quntity, orders.order_date FROM orders,inventory WHERE orders.model=inventory.model");
# 	rows=cursor.fetchall()
# 	for row in rows:
# 		print(row[0],row[1])
# 		print(row[2])
# 		print(row[3])
# 		print("")

#########       or       ############
with sqlite3.connect("cars.db") as connection:
	cursor=connection.cursor()
	cursor.execute("SELECT orders.make,orders.model,inventory.quntity, orders.order_date FROM orders INNER JOIN inventory ON orders.model=inventory.model");
	rows=cursor.fetchall()
	for row in rows:
		print(row[0],row[1])
		print(row[2])
		print(row[3])
		print("")

