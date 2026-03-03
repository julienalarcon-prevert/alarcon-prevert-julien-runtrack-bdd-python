import mysql.connector

try : 
    db = mysql.connector.connect(
        host ="localhost",
        user = "julien_dev",
        password = "password123",
        database = "LaPlateforme"
    )

    cursor = db.cursor()

    cursor.execute("SELECT SUM(superficie) FROM etage")

    resultat = cursor.fetchone()

    superficie_totale = resultat[0]

    print(f"La superficie de la plateforme est de {superficie_totale} m2")

except mysql.connector.Error as e:
    print(f"Erreur de connexion : {e}")

finally:
    if 'db' in locals() and db.is_connected():
        cursor.close()
        db.close()