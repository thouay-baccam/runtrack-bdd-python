import mysql.connector

connexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Teddy2212!",
            database="LaPlateforme"
)

curseur = connexion.cursor()
curseur.execute("SELECT SUM(capacite) FROM salle")
resultat = curseur.fetchone()

print(f"La capacité de toutes les salles est de : {resultat[0]}")

