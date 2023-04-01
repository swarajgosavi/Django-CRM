import mysql.connector

database = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='root'
)

# prepare a cursor object
cursorObject = database.cursor()

#  Create a database
cursorObject.execute("CREATE DATABASE alphonso")

print("All Done!")