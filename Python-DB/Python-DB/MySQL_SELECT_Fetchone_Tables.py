import mysql.connector
 
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Madrika",
  database="Madrika"
)
 
mycursor = mydb.cursor()
 
mycursor.execute("SELECT * FROM customers")
 
myresult = mycursor.fetchone()
 
print(myresult)