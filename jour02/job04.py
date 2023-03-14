import mysql.connector

bd = mysql.connector.connect(
    host="localhost",
    user="test",
    password="abcd1234,;:!ABCD",
    database="LaPlateforme"
)

cur = bd.cursor()

cur.execute("select nom, capacite from salles")

resultats = cur.fetchall()

print(resultats)