#!/usr/bin/python3
import MySQLdb
import sys

"""Connect to MySQL database and retrieve data from the "states" table"""
# Establish a connection to the MySQL database using input arguments
db = MySQLdb.connect(host="localhost",
                     user=str(sys.argv[1]),
                     passwd=(sys.argv[2]),
                     db=str(sys.argv[3]),
                     port=3306
                     )
# Create a cursor object to execute queries
mycursor = db.cursor()

# Execute a SELECT query to retrieve all rows from the "states" table
mycursor.execute("SELECT * FROM states ORDER BY id ASC")

if __name__ == "__main__":
    # Retrieve all rows returned by the query
    rows = mycursor.fetchall()
    # Print each row to the console
    for row in rows:
        print(row)

# Close the cursor and database connections
mycursor.close()
db.close()
