from person import Person
from cars import Car
from db_mabeger import DatabaseManager
from db_csv_maneger import CSVManager



p1=Person(1,"daniel",22,"daniel213126@.com")
d1=DatabaseManager()
d1.create_tables()
# d1.insert_person(p1)
# print(d1.get_person_by_id(1))
# print(d1.get_all_persons())

c1=CSVManager()
c1.export_persons_to_csv([p1],"db_csv_persons.csv")