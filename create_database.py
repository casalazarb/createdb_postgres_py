#create a new database
#import the libraries
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

#Ask the user for the database name

database = input('database name:')

#ask the user for the data nedeed for the connection

username = input('username:')
passwd = input('password:')
port_id = input('port:')

#set a connection
try:

    conn = psycopg2.connect(user = username, password = passwd, port = port_id)
    #Autocommit to create the database from pyscopg2
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

except Exception as error:

    print(error)

#create a cursor
cur = conn.cursor()

#create database in sql

sql_create_database = 'CREATE DATABASE ' + database + ';'
print(sql_create_database)
#create a table in postgres database
cur.execute(sql_create_database)

conn.close()
