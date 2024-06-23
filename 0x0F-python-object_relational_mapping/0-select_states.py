#!/usr/bin/python3
""" lists all states from the database"""
import MySQLdb
import sys

if __name__ == "__name__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, user=mysql_username, password=mysql_password, db=database_name)

    cursor = db.cursor()


    cursor.execute("SELECT * FROM states ORDER id ASC")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
