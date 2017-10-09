import sqlite3

#############    assignment 1     ##############

# with sqlite3.connect("cars.db") as connection:
# 	c=connection.cursor()

# 	sql={
# 		"Focus count ": "SELECT COUNT(make) from orders WHERE model='Focus'",
# 		"Civic count ": "SELECT COUNT(make) from orders WHERE model='Civic'",
# 		"Ranger count ":"SELECT COUNT(make) from orders WHERE model='Ranger'",
# 		"Accord count" : "SELECT COUNT(make) from orders WHERE model='Accord'",
# 		"Avenger count": "SELECT COUNT(make) from orders WHERE model='Avenger'" 
# 	}

# 	for keys, values in sql.items():
# 		c.execute(values)
# 		row=c.fetchone()
# 		print(keys+" :", row[0])

###########     assignment 2      ###############

with sqlite3.connect("cars.db") as connection:
	c=connection.cursor()
	c.execute("SELECT * from inventory")
	row=c.fetchall()
	for i in row:
		print(i[0], i[1])
		print(i[2])
		c.execute("SELECT COUNT(order_date) from orders WHERE make=? and model=?",(i[0],i[1]))
		print(c.fetchone()[0])