import mysql.connector
import datetime

def connectsql():
    return mysql.connector.connect(
        host='localhost',
        database='zoo',
        user='root',
        password='Teddy2212!')

def ajoutanimal(nom, race, id_cage, date_naissance, pays_origine):
    connection = connectsql()
    cursor = connection.cursor()
    query = "INSERT INTO animal (nom, race, id_cage, date_naissance, pays_origine) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, (nom, race, id_cage, date_naissance, pays_origine))
    connection.commit()
    connection.close()

def animalremove(id_animal):
    connection = connectsql()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM animal WHERE id = %s", (id_animal,))
    connection.commit()
    connection.close()

def majanimal(id_animal, nom=None, race=None, id_cage=None, date_naissance=None, pays_origine=None):
    connection = connectsql()
    cursor = connection.cursor()
    query = "UPDATE animal SET "
    params = []
    if nom:
        query += "nom = %s, "
        params.append(nom)
    if race:
        query += "race = %s, "
        params.append(race)
    if id_cage:
        query += "id_cage = %s, "
        params.append(id_cage)
    if date_naissance:
        query += "date_naissance = %s, "
        params.append(date_naissance)
    if pays_origine:
        query += "pays_origine = %s, "
        params.append(pays_origine)
    query = query.rstrip(", ")
    query += " WHERE id = %s"
    params.append(id_animal)
    cursor.execute(query, tuple(params))
    connection.commit()
    connection.close()

def animallist():
    connection = connectsql()
    cursor = connection.cursor()
    cursor.execute("SELECT animal.*, cage.superficie FROM animal LEFT JOIN cage ON animal.id_cage = cage.id")
    animals = cursor.fetchall()
    connection.close()
    return animals

def superficiecage():
    connection = connectsql()
    cursor = connection.cursor()
    cursor.execute("SELECT SUM(superficie) FROM cage")
    total = cursor.fetchone()[0]
    connection.close()
    return total

def ajoutcage(superficie, capacite_max):
    connection = connectsql()
    cursor = connection.cursor()
    query = "INSERT INTO cage (superficie, capacite_max) VALUES (%s, %s)"
    cursor.execute(query, (superficie, capacite_max))
    connection.commit()
    connection.close()

def supprimecage(id_cage):
    connection = connectsql()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM cage WHERE id = %s", (id_cage,))
    connection.commit()
    connection.close()

def majcage(id_cage, superficie=None, capacite_max=None):
    connection = connectsql()
    cursor = connection.cursor()
    query = "UPDATE cage SET "
    params = []
    if superficie is not None:
        query += "superficie = %s, "
        params.append(superficie)
    if capacite_max is not None:
        query += "capacite_max = %s, "
        params.append(capacite_max)
    query = query.rstrip(", ")
    query += " WHERE id = %s"
    params.append(id_cage)
    cursor.execute(query, tuple(params))
    connection.commit()
    connection.close()

ajoutcage(200, 20)
ajoutanimal("Leo", "Lion", 1, "2010-04-25", "Kenya")
ajoutcage(150, 10)
majcage(2, superficie=200.0)
print(animallist())
animalremove(1)
supprimecage(1)
ajoutanimal("Bingus", "Chat Sphinx", 2, "2020-03-29", "Amerique")
ajoutanimal("Maxwell", "Chat Tuxedo", 2, "2019-05-19", "Amerique")
majanimal(2, nom="Plink")
print(animallist())
print(superficiecage())