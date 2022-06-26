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

table_names = ['orders', 'users']

columns_names = ['(user_id, pizza_type)', '(user_id, name, address)']

list_values = [
[(133, 'Mariana'),
(133, 'Diavola'),
(257, 'Margherita'),
(344, 'Vegetables'),
(441, 'Vegetables'),
(777, 'Pepperoni'),
(777, 'Meatballs'),
(777, 'Vegetables'),
(555, 'Fratelanza'),
(555, 'Porto'),
(122, 'Capodimonte'),
(122, 'Marinara'),
(257, 'Diavola')],
[(133, 'Mitch', '35 Springfield Ave.'),
(257, 'Sue', '87 Pine St.'),
(441, 'Lee', '37 Columbus Ave.'),
(344, 'Lolo', '88 Market St.'),
(777, 'Cali', '77 Mulholland Dr.'),
(555, 'Wendy', '56 Sutro Blvd.'),
(122, 'Analu', '11 Drumm St.')]
]

#loop to insert the values in the tables
for table, columns, list in zip(table_names, columns_names, list_values):
    #insert each value of the list
    for value in list:
        #sql statement to insert
        sql_insert_value = 'INSERT INTO ' + table + ' ' + columns + ' VALUES '
        print(sql_insert_value, value)
        #create a table in postgres database
        cur.execute(sql_insert_value + str(value))

#Commit to make the changes
conn.commit()

#Close the connection
conn.close()
