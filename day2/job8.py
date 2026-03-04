import mysql.connector as mysql

class DatabaseManager:
    def __init__(self, host, user, password, database):
        self.connection = mysql.connect(
            host = host, user = user, password = password, database = database
            )
        self.cursor = self.connection.cursor(buffered=True)

    def execute (self, query, params=None):
        self.cursor.execute(query, params)
        if query.strip().upper().startswith("SELECT"):
            return self.cursor.fetchall()
        self.connection.commit()
        return True
    
    def close(self):
        self.cursor.close()
        self.connection.close()

class CageManager:
    def __init__(self, db_manager):
        self.db = db_manager

    def ajouter_cage(self, superficie, capacite_max):
        sql = "INSERT INTO cage (superficie, capacite_max) VALUES (%s, %s)"
        self.db.execute(sql, (superficie, capacite_max))
    
    def superficie_total(self):
        sql = "SELECT SUM(superficie) FROM cage"
        resultat = self.db.execute(sql)
        return resultat[0][0] if resultat else 0
    
class AnimalManager:
    def __init__(self, db_manager):
        self.db = db_manager

    def ajouter_animal(self, nom, race, id_cage, date_naissance, pays):
        sql = "INSERT INTO animal(nom, race, id_cage, date_naissance, pays_origine) VALUES (%s, %s, %s, %s, %s)"
        self.db.execute(sql,(nom, race, id_cage, date_naissance, pays))

    def liste_animaux(self):
        return self.db.execute("SELECT * FROM animal")
    

mon_db_manager = DatabaseManager("localhost", "julien_dev", "password123", "zoo")
gestion_cages = CageManager(mon_db_manager)
gestion_animaux = AnimalManager(mon_db_manager)

while True:
    print("\n--- GESTION DU ZOO ---")
    print("1. Ajouter une cage")
    print("2. Ajouter un animal")
    print("3. Voir tous les animaux")
    print("4. Voir la superficie totale du zoo")
    print("5. Quitter")
    
    choix = input("Choisissez une option : ")

    if choix == "1":
        sup = input("Superficie : ")
        capa = input("Capacité max : ")
        gestion_cages.ajouter_cage(sup, capa)
        print("Cage ajoutée !")

    elif choix == "2":
        nom = input("Nom de l'animal : ")
        race = input("Race : ")
        id_cage = input("ID de la cage : ")
        date_n = input("Date naissance (AAAA-MM-JJ) : ")
        pays = input("Pays d'origine : ")
        gestion_animaux.ajouter_animal(nom, race, id_cage, date_n, pays)
        print("Animal ajouté !")

    elif choix == "3":
        animaux = gestion_animaux.liste_animaux()
        for a in animaux:
            print(a)

    elif choix == "4":
        total = gestion_cages.superficie_total()
        print(f"La superficie totale du zoo est de : {total} m²")

    elif choix == "5":
        print("Fermeture du programme...")
        mon_db_manager.close()
        break
    
    else:
        print("Option invalide.")