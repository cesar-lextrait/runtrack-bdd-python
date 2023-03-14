import mysql.connector

bd = mysql.connector.connect(
    host="localhost",
    user="test",
    password="abcd1234,;:!ABCD",
    database="LaPlateforme"
)

cur = bd.cursor()

etage1 = "insert into etage (nom, numero, superficie) values (%s, %s, %s)"
values1 = ("RDC", 0, 500)
cur.execute(etage1, values1)

etage2 = "insert into etage (nom, numero, superficie) values (%s, %s, %s)"
values2 = ("R+1", 1, 500)
cur.execute(etage2, values2)

lounge = "insert into salles (nom, id_etage, capacite) values (%s, %s, %s)"
values3 = ('Lounge', 1, 100)
cur.execute(lounge, values3)

studio_son = "insert into salles (nom, id_etage, capacite) values (%s, %s, %s)"
values4 = ('Studio son', 1, 5)
cur.execute(studio_son, values4)

broadcasting = "insert into salles (nom, id_etage, capacite) values (%s, %s, %s)"
values5 = ('Broadcasting', 2, 50)
cur.execute(broadcasting, values5)

bocalpPeda = "insert into salles (nom, id_etage, capacite) values (%s, %s, %s)"
values6 = ('Bocal pPeda', 2, 4)
cur.execute(bocalpPeda, values6)

coworking = "insert into salles (nom, id_etage, capacite) values (%s, %s, %s)"
values7 = ('Coworking', 2, 80)
cur.execute(coworking, values7)

studio_video = "insert into salles (nom, id_etage, capacite) values (%s, %s, %s)"
values8 = ('Studio video', 2, 5)
cur.execute(studio_video, values8)

bd.commit()

print(cur.rowcount, "record inserted.")