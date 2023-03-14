import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="test",
    password="abcd1234,;:!ABCD",
    database="LaPlateforme"
)

print(mydb)


mycursor = mydb.cursor()
mycursor.execute("select * from ettudiants")
myresult = mycursor.fetchall()
for row in myresult:
    print(row)
