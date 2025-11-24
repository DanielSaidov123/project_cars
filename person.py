from datetime import datetime
import sqlite3
import csv
class Person:
    def __init__(self, person_id, name, age, email):
        self.person_id = person_id
        self.name = name
        self.age = age
        self.email = email
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def get_cars_count(self):
        print(len(self.cars))

    def __str__(self):
        return f"person_id: {self.person_id},name: {self.name}, age: {self.age},email: {self.email}  "

    def to_dict(self):
        return {"person_id":self.person_id,
                "name":self.name,
                "age":self.age,
                "email":self.email,
                "cars":[car for car in self.cars]}



    



