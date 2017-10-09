#sql joins
import sqlite3
with sqlite3.connect("new.db") as connection:
	c=connection.cursor()
	c.execute("SELECT population.city, population.population, regions.region from population, regions where population.city=regions.city")
	
	rows=c.fetchall()
	for r in rows:
		print(r)	