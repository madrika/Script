import mysql.connector
mydb = mysql.connector.connect(host="localhost", 
user="root", 
password = "Madrika",
database = "Madrika"
)

mycursor = mydb.cursor()
sql = "DELETE FROM customers WHERE address = 'Mountain 21' "
mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted!")
