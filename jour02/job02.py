import mysql.connector


bd = mysql.connector.connect(
    host="localhost",
    user="test",
    password="abcd1234,;:!ABCD",
    database="LaPlateforme"
)

cur = bd.cursor()
cur.execute("create table etage (id int not null auto_increment primary key, nom varchar(255), numero int, superficie int)")
cur.execute("create table salles (id int not null auto_increment primary key, nom varchar(255), id_etage int, capacite int)")
