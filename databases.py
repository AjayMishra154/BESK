import sqlite3

conn = sqlite3.connect("Besk.db")
print("open database")
#
# conn.execute("create table users(user VARCHAR(15) PRIMARY KEY, password VARCHAR(10) NOT NULL)")


conn.execute("create table Book(Name VARCHAR(50), Book_Name VARCHAR(30), Description VARCHAR(200), image VARCHAR ,"
             " email VARCHAR(50) NOT NULL)")
print("table created")