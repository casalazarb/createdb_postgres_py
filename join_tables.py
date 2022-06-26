#import the libraries
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

#sql statement
sql_join = 'SELECT orders.user_id, orders.pizza_type, users.address\
            FROM orders\
            INNER JOIN users\
            on orders.user_id = users.user_id;'

cur.execute(sql_join)

#store the result in the variable
result = cur.fetchall()

#print each row
for row in result:
    print(row)

conn.commit()

conn.close()
