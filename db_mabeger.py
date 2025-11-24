from person import Person
from cars import Car
from datetime import datetime
import sqlite3

class DatabaseManager:
    def __init__(self, db_name="db_daniel.db"):
        import sqlite3
        self.db_name = db_name
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()

    def create_tables(self):
        
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS persons (
        person_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        email TEXT UNIQUE NOT NULL
            )
        ''')

        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS cars (
        car_id INTEGER PRIMARY KEY,
        brand TEXT NOT NULL,
        model TEXT NOT NULL,
        year INTEGER NOT NULL,
        color TEXT NOT NULL,
        owner_id INTEGER,
        FOREIGN KEY (owner_id) REFERENCES persons(person_id)
        )
        ''')

        self.connection.commit()
        print("✓ Table created!")




    def insert_person(self, person:Person):
        try:
            self.cursor.execute("""
                INSERT INTO persons (person_id, name, age, email)
                VALUES (?, ?, ?, ?)
            """, (person.person_id, person.name, person.age, person.email))

            self.connection.commit()
            print(f"Person {person.name} inserted successfully.")
        
        except sqlite3.IntegrityError as e:
            print("Error inserting person:", e)

    def insert_car(self, car:Car):
        try:
            self.cursor.execute("""
            INSERT INTO cars (car_id,brand,model,year,color,owner_id) 
            VALUES (?, ?, ?, ?)
                    """ ,(car.car_id,car.brand,car.model,car.year,car.color,car.owner_id))
            
        except sqlite3.IntegrityError as e:
            print("Error inserting car:", e)
        

    def get_all_persons(self):
        self.cursor.execute("SELECT person_id, name, age, email FROM persons")
        rows = self.cursor.fetchall()

        persons = []

        for row in rows:
            person_id, name, age, email = row
            p = Person(person_id, name, age, email)
            persons.append(p)

        return persons

    def get_all_cars(self):
        self.cursor.execute("SELECT car_id,brand,model,year,color,owner_id FROM cars")
        rows = self.cursor.fetchall()

        cars = []

        for row in rows:
            car_id,brand,model,year,color,owner_id = row
            c = Car(car_id,brand,model,year,color,owner_id)
            cars.append(c)

        return cars

    def get_person_by_id(self, person_id):
        self.cursor.execute("SELECT * FROM persons WHERE person_id=?", (person_id,))
        row = self.cursor.fetchone()
        if row:
            return row  
        else:
            print("Person not found")
            return None

    def get_cars_by_owner(self, owner_id):
        self.cursor.execute("SELECT car_id, brand, model, year, color, owner_id FROM cars WHERE owner_id=?", (owner_id,))
        rows = self.cursor.fetchall()
        
        if rows:
            cars = []
            for row in rows:
                car_id, brand, model, year, color, owner_id = row
                cars.append(Car(car_id, brand, model, year, color, owner_id))
            return cars
        else:
            print("No cars found for this owner")
            return []

        

    def update_person(self, person: Person):
        self.cursor.execute("SELECT * FROM person WHERE person_id=?", (person.person_id,))
        row = self.cursor.fetchone()
        if row:
            self.cursor.execute("""
                UPDATE person 
                SET name=?, age=?, email=? 
                WHERE person_id=?
            """, (person.name, person.age, person.email, person.person_id))
            self.conn.commit()
            print("Person updated successfully")
        else:
            print("Person not found")
                
    def delete_person(self, person_id):
        """Delete person from database"""
        self.cursor.execute("SELECT * FROM person WHERE person_id=?", (person_id,))
        row = self.cursor.fetchone()
        if row:
            self.cursor.execute("DELETE FROM person WHERE person_id=?", (person_id,))
            self.conn.commit()
            print(f"Person with ID {person_id} deleted successfully")
        else:
            print("Person not found")


    def close(self):
        """Close database connection"""
        self.connection.close()



