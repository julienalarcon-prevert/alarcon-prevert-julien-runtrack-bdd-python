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

class Employe:
    def __init__(self, db_manager):
        self.db = db_manager

    def create(self, nom, prenom, salaire, id_service):
        sql = "INSERT INTO employe (nom, prenom, salaire, id_service) VALUES (%s, %s, %s, %s)"
        self.db.execute(sql, (nom, prenom, salaire, id_service))

    def read_all(self):
        return self.db.execute("SELECT * FROM employe")

    def update_salary (self, id_employe, new_salaire):
        sql = "UPDATE employe SET salaire = %s WHERE id = %s"
        self.db.execute(sql, (new_salaire, id_employe))
    
    def delete(self, id_employe):
        sql = "DELETE FROM employe WHERE id = %s"
        self.db.execute(sql, (id_employe))

mngr = DatabaseManager("localhost", "julien_dev", "password123", "Personnel")
repo = Employe(mngr)

print("ADD employe")
repo.create("Dupont", "Jean", 3500, 1)

print("Liste des employes")
print(repo.read_all())

print("Update salaire")
repo.update_salary(1, 4000)

mngr.close()