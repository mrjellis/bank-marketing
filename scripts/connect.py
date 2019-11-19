import psycopg2
import pandas as pd
import pandas.io.sql as psql

#utlizes psycopg2 to connect to the postgresql database I created from the csv in /Data folder.

db_name = 'bank-marketing'
db_user = 'postgres'
db_password = ''
db_host = 'localhost'
db_port = 5432

#attempts connecting to the database
try:
    conn = psycopg2.connect(database=db_name,user=db_user,password=db_password,host=db_host,port=db_port)


    print("Database connected succesful")
except:
    print("No luck")



#declare data variable
df = psql.read_sql("SELECT * FROM bank",conn)

