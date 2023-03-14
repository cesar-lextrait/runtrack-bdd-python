import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="test",
    password="abcd1234,;:!ABCD",
    database="LaPlateforme"
)

cur = db.cursor()

cur.execute("select sum(superficie) from etage")
resultat = cur.fetchone()[0]

print("La superficie de la La Plateforme est de ",resultat, "m2")