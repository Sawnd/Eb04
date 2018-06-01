#!/usr/bin/python
import mysql.connector as connector

# Connect
db = connector.connect(host="localhost",
                       user="eb04",
                       passwd="coolos3022",
                       db="eb04")

cursor = db.cursor()

# Execute SQL select statement
#cursor.execute("SELECT * FROM temperature")
# Commit your changes if writing
# In this case, we are only reading data
# db.commit()

# Get the number of rows in the resultset
# numrows = cursor.rowcount
#
# # Get and display one row at a time
# for x in range(0, numrows):
#     row = cursor.fetchone()
#     print row[0], "-->", row[1]
#
# # Close the connection
# db.close()