class Animal:
    def __init__(self, name, species, cage_id, birth_date, origin_country):
        self.name = name
        self.species = species
        self.cage_id = cage_id
        self.birth_date = birth_date
        self.origin_country = origin_country

    def save(self, db):
        query = "INSERT INTO animal (name, species, cage_id, birth_date, origin_country) VALUES (%s, %s, %s, %s, %s)"
        db.execute_query(query, (self.name, self.species, self.cage_id, self.birth_date, self.origin_country))

    def delete(db, animal_id):
        db.execute_query("DELETE FROM animal WHERE id = %s", (animal_id,))

    @staticmethod
    def get_all(db):
        return db.execute_query("SELECT * FROM animal")

    # Additional methods for updating and other operations can be added here
