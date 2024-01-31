class Cage:
    def __init__(self, size, max_capacity):
        self.size = size
        self.max_capacity = max_capacity

    def save(self, db):
        query = "INSERT INTO cage (size, max_capacity) VALUES (%s, %s)"
        db.execute_query(query, (self.size, self.max_capacity))

    def delete(db, cage_id):
        db.execute_query("DELETE FROM cage WHERE id = %s", (cage_id,))

    @staticmethod
    def get_all(db):
        return db.execute_query("SELECT * FROM cage")

    # Additional methods for updating and other operations can be added here
