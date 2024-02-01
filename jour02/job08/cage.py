class Cage:
    def __init__(self, superficie, capacite_max):
        self.superficie = superficie
        self.capacite_max = capacite_max

    def save(self, db):
        query = "INSERT INTO cage (superficie, capacite_max) VALUES (%s, %s)"
        db.execute_query(query, (self.superficie, self.capacite_max))

    def update(self, db, id_cage):
        query = "UPDATE cage SET superficie = %s, capacite_max = %s WHERE id = %s"
        db.execute_query(query, (self.superficie, self.capacite_max, id_cage))

    def delete(db, cage_id):
        db.execute_query("DELETE FROM cage WHERE id = %s", (cage_id,))

    @staticmethod
    def get_all(db):
        return db.execute_query("SELECT * FROM cage")

    # Additional methods for updating and other operations can be added here
