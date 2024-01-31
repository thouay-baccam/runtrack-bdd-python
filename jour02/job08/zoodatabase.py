import mysql.connector

class ZooDatabase:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password

    def connect(self):
        return mysql.connector.connect(
            host=self.host,
            database=self.database,
            user=self.user,
            password=self.password
        )

    def execute_query(self, query, params=()):
        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute(query, params)
        if query.strip().upper().startswith("SELECT"):
            result = cursor.fetchall()
        else:
            connection.commit()
            result = None
        connection.close()
        return result
