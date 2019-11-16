import psycopg2
import pandas as pd
import pandas.io.sql as psql

db_name = 'bank-marketing'
db_user = 'postgres'
db_password = 'myfile1'
db_host = 'localhost'
db_port = 5432

try:
    conn = psycopg2.connect(database=db_name,user=db_user,password=db_password,host=db_host,port=db_port)


    print("Database connected succesful")
except:
    print("No luck")




df = psql.read_sql("SELECT * FROM bank",conn)
