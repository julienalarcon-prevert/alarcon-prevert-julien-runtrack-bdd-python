import mysql.connector

try : 
    db = mysql.connector.connect(
        host ="localhost",
        user = "julien_dev",
        password = "password123",
        database = "LaPlateforme"
    )

    cursor = db.cursor()

    cursor.execute("SELECT * FROM etudiants")

    etudiants = cursor.fetchall()

    print("Liste des étudiants :")
    for etudiant in etudiants:
        print(etudiant)

except mysql.connector.Error as e:
    print(f"Erreur de connexion : {e}")

finally:
    if 'db' in locals() and db.is_connected():
        cursor.close()
        db.close()