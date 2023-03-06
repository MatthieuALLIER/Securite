import mysql.connector

def connexion(host, user, password, database) :

    mydb = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
    )
    
    return mydb
