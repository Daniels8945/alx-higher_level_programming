#!/usr/bin/python3
""" lists all states from the database"""
import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit()
    #Retrive argumnts
    mysql_username, mysql_password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]
    
    # connect to mysql db
    db = MySQLdb.connect(host="localhost", port=3306, user=mysql_username, password=mysql_password, db=database_name)
    
    # create a cursor object
    cursor = db.cursor()
    
    # Evecute the query
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
