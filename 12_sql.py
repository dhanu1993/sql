#sql functions

import sqlite3
with sqlite3.connect("new.db") as connection:
	c=connection.cursor()

	sql={
		'average':"SELECT AVG(population) from population",
		'maximum':"SELECT MAX(population) from population",
		'minimum':"SELECT MIN(population) from population",
		'sum':"SELECT SUM(population) from population",
		'count':"SELECT COUNT(population) from population"
	}
	for keys, values in sql.items():
		c.execute(values)
		r=c.fetchone()
		print(keys + ":",r[0])