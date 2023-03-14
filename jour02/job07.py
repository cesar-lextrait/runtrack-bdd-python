import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="test",
    password="abcd1234,;:!ABCD",
    database="LaPlateforme"
)

cur = db.cursor()

cur.execute("DROP TABLE IF EXISTS employes")
cur.execute("CREATE TABLE employes (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, nom VARCHAR(255), prenom VARCHAR(255), salaire DECIMAL(10,2), id_service INT)")


employes = [
    ( "Doe", "John", 1000.13, 1),
    ( "Doe", "Jane", 4000.13, 3),
    ( "Fadeup", "Jack", 13900.13, 2),
    ( "Pullup", "Jill", 1040.13, 4),
    ( "Azo", "Jenny", 600.323, 5),
    ( "Zoro", "Jen", 10320.00, 6),
    ( "Totz", "John", 2900.92, 7),
    ( "Grrr", "azerty", 1900.49, 8),
]

for employe in employes:
    cur.execute("insert into employes (nom, prenom, salaire, id_service) values (%s, %s, %s, %s)", employe)
    db.commit()

cur.execute("DROP TABLE IF EXISTS  services")
cur.execute("create table services (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, nom VARCHAR(255))")
services = [
    ("Comptabilité"),
    ("Informatique"),
    ("Ressources Humaines"),
    ("Communication"),
    ("Juridique"),
    ("Direction"),
    ("Marketing"),
    ("Administration"),
    ("Production"),
    ("Maintenance"),
    ("Sécurité"),
    ("Logistique"),
]

for service in services:
    cur.execute("insert into services (nom) values (%s)", (service,))
    db.commit()

cur.execute("SELECT employes.nom, employes.prenom, services.nom FROM employes LEFT JOIN services ON employes.id_service = services.id")
result = cur.fetchall()
for row in result:
    print(row)


cur.execute("SELECT employes.nom, employes.prenom, CAST(salaire AS signed) as salaire, services.nom FROM employes LEFT JOIN services ON employes.id_service = services.id WHERE salaire > 3000")
result = cur.fetchall()
for row in result:
    print(row)

class Salaries:
    def __init__(self, nom, prenom, salaire, id_service):
        self.nom = nom
        self.prenom = prenom
        self.salaire = salaire
        self.id_service = id_service
        self.connexion = mysql.connector.connect(
            host="localhost",
            user="test",
            password="abcd1234,;:!ABCD",
            database="LaPlateforme"
        )
        self.curseur = self.connexion.cursor()

    def create(self, nom, prenom, salaire, id_service):
        query = "INSERT INTO employes (nom, prenom, salaire, id_service) VALUES (%s, %s, %s, %s)"
        values = (nom, prenom, salaire, id_service)
        self.curseur.execute(query, values)
        self.connexion.commit()

    def read(self):
        query = "SELECT * FROM employes"
        self.curseur.execute(query)
        return self.curseur.fetchall()
    
    def update(self, id, nom, prenom, salaire, id_service):
        query = "UPDATE employes SET nom = %s, prenom = %s, salaire = %s, id_service = %s WHERE id = %s"
        values = (nom, prenom, salaire, id_service, id)
        self.curseur.execute(query, values)
        self.connexion.commit()

    def delete(self, id):
        query = "DELETE FROM employes WHERE id = %s"
        values = (id,)
        self.curseur.execute(query, values)
        self.connexion.commit()

    def close(self):
        self.curseur.close()
        self.connexion.close()


salaries = Salaries('localhost', 'test', 'abcd1234,;:!ABCD', 'LaPlateforme')
salaries.create("Marxoe", "Bane", 43400.13, 3)

result = salaries.read()
for row in result:
    print(row)

salaries.update(1, "Doe", "John", 2000.13, 1)
