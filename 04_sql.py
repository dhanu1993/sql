#read the records from csv file and insert  into employees table of database
import sqlite3
import csv

with sqlite3.connect("new.db") as connection:
	c=connection.cursor()
	employees = csv.reader(open("employees.csv", "rU"))
	c.execute("CREATE TABLE employees(firstname TEXT, lastname TEXT)")
	c.executemany("INSERT INTO employees(firstname, lastname) VALUES(?,?)", employees)