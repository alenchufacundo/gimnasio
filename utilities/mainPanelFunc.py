from db.db_connection import Database


def loadInfo():
    db = Database()
    db.select_all_user