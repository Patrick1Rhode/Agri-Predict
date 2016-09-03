#!/usr/bin/python
import MySQLdb
# Open database connection
db = MySQLdb.connect("localhost","root","","zambia_weather")
# prepare a cursor object using cursor() method
cursor = db.cursor()
insert = """INSERT INTO test (name, region) VALUES (%s, %s)"""
sql = cursor.execute(insert, ("Hello", "World"))
db.commit()

#cursor.execute(sql)
# disconnect from server
db.close()
# execute SQL query using execute() method.
#cursor.execute("DROP TABLE IF EXISTS employees")
# Fetch a single row using fetchone() method.
# Create table as per requirement
