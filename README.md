# createdb_postgres_py
Create a database in postgresql, create tables, insert values, create a join query with python psycopg2.

You have to install first postgresql in your local machine.
Change the pg_hba.conf file to modify the authentication method to md5, using nano text editor is an easy way.
Install psycopg2, use pip.

file create_database.py
connect to postgresql and create a database with the name provided by the user, enter the username, password and port when running
the python file.

file create_tables.py
connect to postgresql and create the tables or relations in the database, to provide information of the name of the tables and 
the columns, change the .py file, use lists and tuples. Enter the name of the already created database, the username, password and port
after you have run the python file.

file insert_values.py
connect to postgresql and insert the values in each table, to provide information of the values to be inserted and 
the columns. change the .py file, use a list of tuples to insert several values. Enter the name of the already created database
the username, password and port, after you have run the python file.

file join_tables.py
You need to know the distribution of flavors according to the location, you can make an inner join that allow you to know  the locations 
where different flavors of pizza are being delivered. Change the query according to your needs.
