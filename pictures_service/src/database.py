"""
Database
Module with the database methods used by the handlers of the service
This module will use SQLite as the database for prototyping
"""
import sqlite3


class Database:
    """
    Database class with the methods to handle the required Database operations
    """

    def __init__(self, database_file: str):
        self.database_file = database_file

    def execute_query(self, query: str, args=None) -> list:
        conn = sqlite3.connect(self.database_file)
        cursor = conn.cursor()
        rows = cursor.execute(query, args)
        conn.commit()
        conn.close()
        return rows.fetchall()
