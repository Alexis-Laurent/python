import mysql.connector 

connection = mysql.connector.connect(host="localhost",user="root",password="",database="produit")

curs = connection.cursor()
curs.execute("""SELECT * FROM produit""")
rows = curs.fetchall()
for item in rows:
   print(item)

connection.close
