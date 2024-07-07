from db.abstract_database import AbstractDatabase

import json
from typing import Any


class JSONDatabase(AbstractDatabase):
    def __init__(self, json_file: str):
        self.json_file = json_file
        self.data = []

    def connect(self):
        try:
            with open(self.json_file, 'r') as file:
                self.data = json.load(file)
        except FileNotFoundError:
            self.data = []

    def disconnect(self):
        try:
            with open(self.json_file, 'w') as file:
                json.dump(self.data, file, indent=4)
        except Exception as e:
            print(f"Error saving JSON file: {e}")

    def execute_query(self, query: str):
        # For JSON database, query might be operations like insert, update, delete,
        # but here we'll focus on basic operations
        pass

    def fetch_one(self) -> Any:
        if self.data:
            return self.data[0]
        return None

    def fetch_all(self) -> list:
        return self.data
