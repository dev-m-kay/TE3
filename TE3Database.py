"""
Created using this tutorial: https://www.youtube.com/watch?v=lFRMdGfo_XA&t=55s
Modified to allow User input
"""

import sqlite3

class Person:
    def __init__(self, id_num=-1, first="", last="", age=-1):
        self.id_num = id_num
        self.first = first
        self.last = last
        self.age = age
        self.connection = sqlite3.connect('mydata.db')
        self.cursor = self.connection.cursor()

    def load_person(self, id_num):
        self.cursor.execute("""
        SELECT * FROM persons
        WHERE id = {}
        """.format(id_num))

        results = self.cursor.fetchone()

        self.id_num = id_num
        self.first = results[1]
        self.last = results[2]
        self.age = results[3]

    def insert_person(self):
        self.cursor.execute("""
        INSERT INTO persons VALUES
        ({}, '{}', '{}', {})
        """.format(self.id_num, self.first, self.last, self.age))

        self.connection.commit()
        self.connection.close()

connection = sqlite3.connect('mydata.db')
cursor = connection.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS persons (
    id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    age INTEGER
)
""")
connection.commit()
connection.close()


fname = input("Enter your first name: ")
lname = input("Enter your last name: ")
age = int(input("Enter your age: "))
num = int(input("Enter an id number: "))
p1 = Person(num, fname, lname, age)
p1.insert_person()

connection = sqlite3.connect('mydata.db')
cursor = connection.cursor()

cursor.execute("SELECT * FROM persons")
results = cursor.fetchall()
print(results)

connection.close()
