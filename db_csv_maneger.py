import csv
from person import Person
from cars import Car
from db_mabeger import DatabaseManager


class CSVManager:
    @staticmethod
    def export_persons_to_csv(persons, filename):
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            
            writer.writerow(['person_id', 'name', 'age', 'email'])
            
            for person in persons:
                writer.writerow([person.person_id, person.name, person.age, person.email])

        print(f"Exported {len(persons)} persons to {filename}")
    
    @staticmethod
    def export_cars_to_csv(cars, filename):
        with open(filename,mode="w",newline='' , encoding='utf-8')as file:
            writer =csv.writer(file)

            writer.writerow(["car_id","brand","model","year","color","owner_id"])
            for car in cars:
                writer.writerow([cars.car_id,cars.brand,cars.model,cars.year,cars.color,cars.owner_id])
        print(f"Exported {len(cars)} car to {filename}")
    
    @staticmethod
    def import_persons_from_csv(filename):
        persons=[]
        with open(filename,mode="r",newline='',encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                person_id = int(row[0])
                name = row[1]
                age = int(row[2])
                email = row[3]
                persons.append(Person(person_id,name,age,email))

        return persons
    
                
    @staticmethod
    def import_cars_from_csv(filename):
        cars=[]
        with open(filename,mode="r",newline='',encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                car_id = int(row[0])
                brand = row[1]
                model = row[2]
                year = int(row[3])
                color=row[4]
                owner_id=int(row[5])
                cars.append(Car(car_id,brand,model,year,color,owner_id))

        return cars
    
    @staticmethod
    def export_full_report(db_manager:DatabaseManager, filename):
         
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            
            writer.writerow(['person_name', 'age', 'email', 'cars_count', 'car_brands'])
            
            persons = db_manager.get_all_persons()
            
            for person in persons:
                cars = db_manager.get_cars_by_owner(person.person_id)
                
                cars_count = len(cars)
                car_brands = ','.join([car.brand for car in cars])
                
                writer.writerow([person.name, person.age, person.email, cars_count, car_brands])
        
        print(f"Full report exported to {filename}")

