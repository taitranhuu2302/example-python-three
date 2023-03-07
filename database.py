import mysql.connector


def connectDb():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="db"
    )
