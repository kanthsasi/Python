import mysql.connector

con=mysql.connector.connect(host="localhost",user="root",passwd="root",database="db")
cur=con.cursor()
dbs=cur.execute("select*from db;")
for x in cur:
 print(x)