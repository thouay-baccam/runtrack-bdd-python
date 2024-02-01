import mysql.connector

def connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Teddy2212!",
        database="lethalcompany"
    )

def employeriche(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employe WHERE salaire > 3000")
    for employe in cursor.fetchall():
        print(employe)

def employeservice(conn):
    cursor = conn.cursor()
    cursor.execute("""
    SELECT e.nom, e.prenom, s.nom AS service_name
    FROM employe e
    INNER JOIN service s ON e.id_service = s.id
    """)
    for employe in cursor.fetchall():
        print(employe)

# Connect to the database
conn = connection()

# Perform the operations
print("Employé avec un salaire plus de 3000:")
employeriche(conn)

print("\nEmployés et leur service:")
employeservice(conn)

# Close the connection
conn.close()
