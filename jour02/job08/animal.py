class Animal:
    def __init__(self, nom, race, id_cage, date_naissance, pays_origine):
        self.nom = nom
        self.race = race
        self.id_cage = id_cage
        self.date_naissance = date_naissance
        self.pays_origine = pays_origine

    def save(self, db):
        query = "INSERT INTO animal (nom, race, id_cage, date_naissance, pays_origine) VALUES (%s, %s, %s, %s, %s)"
        db.execute_query(query, (self.nom, self.race, self.id_cage, self.date_naissance, self.pays_origine))

    def update(self, db, id_animal):
        query = "UPDATE animal SET nom = %s, race = %s, id_cage = %s, date_naissance = %s, pays_origine = %s WHERE id = %s"
        db.execute_query(query, (self.nom, self.race, self.id_cage, self.date_naissance, self.pays_origine, id_animal))

    def delete(db, animal_id):
        db.execute_query("DELETE FROM animal WHERE id = %s", (animal_id,))

    @staticmethod
    def get_all(db):
        return db.execute_query("SELECT * FROM animal")

    # Additional methods for updating and other operations can be added here
