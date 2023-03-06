import mysql.connector

def connexion(host, user, password, database) :

    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database=""
    )
    
    return mydb
