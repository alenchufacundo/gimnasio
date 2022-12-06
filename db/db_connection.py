import pymysql

class Database:
    def __init__(self):
        self.connect = pymysql.connect(
            host = "",
            port = "",
            user = "rootafr",
            password = "6338.hola",
            db=""
        )
        self.cursor = self.connect.cursor()

    def select_all_user(self):
        self.sql = "SELECT * FROM alumnos"

        try:
            self.cursor.execute(self.sql)
            users = self.cursor.fetchall()
            for user in users:
                print(user)
        
        except Exception as error:
            raise

    def select_user_by_name(self, name, lastname):
        self.sql = f"SELECT * FROM alumnos WHERE nombre = {name} OR nombre = {lastname}"

        try:
            self.cursor.execute(self.sql)
            user = self.cursor.fetchone
            print(user)

        except Exception as error:
            raise
    
    def delete_user (self,id):
        self.sql = "DELETE FROM alumnos WHERE id = {id} "
        

