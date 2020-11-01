"""Mangaging files"""

#TODO létrehozni egy vagy több osztályt ami ír és olvas fájlokból

import json

class Files:
    def __init__(self, filename):
        self.filename = filename

    def get_json_file(self):
        with open(self.filename, "r") as file:
            data = json.load(file)
            return data

    def write_json_file(self, jsonData):
        with open(self.filename, "w") as file:
            json.dump(jsonData, file)
