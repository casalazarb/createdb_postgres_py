#import libraries
import psycopg2

#ask the user for the data nedeed for the connection

database = input('database name:')
username = input('username:')
passwd = input('password:')
port_id = input('port:')

#set a connetion
try:

    conn = psycopg2.connect(dbname = database, user = username, password = passwd, port = port_id)

except Exception as error:

    print(error)

#create a cursor
cur = conn.cursor()

table_names = ["orders", "users"]

columns_names = ["(user_id int, pizza_type varchar)", "(user_id int, name varchar, address varchar)"]

#create tables statement
for table, columns in zip(table_names, columns_names):
    #SQL statement
    sql_create_table = "CREATE TABLE if not exists " + table + " " + columns + ";"
    print(sql_create_table)
    #create a table in postgres database
    cur.execute(sql_create_table)
    #commit to make the changes
    conn.commit()

conn.close()
