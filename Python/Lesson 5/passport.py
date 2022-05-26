"""
Створіть клас Passport (паспорт), який буде
містити паспортну інформацію про громадянина заданої країни.
За допомогою механізму успадкування, реалізуйте
клас ForeignPassport (закордонний паспорт) похідний від
Passport.
Нагадаємо, що закордонний паспорт містить крім паспортних даних, також дані про візи, номер
закордонний паспорт.

Кожен із класів повинен містити необхідні методи.
"""

import random
import datetime

PASSPORT_INFO = "Passport info:\n\
\tFirst name: {}\n\
\tLast name: {}\n\
\tMiddle name: {}\n\
\tGender: {}\n\
\tBirth date: {}\n\
\tNationality: {}\n\
\tUnit: {}\n\
\tCreated date: {}\n\
\tExpiry date: {}\n\
\tNumber: {}\n"

F_PASSPORT_INFO = "Foreign Passport info:\n\
\tFirst name: {}\n\
\tLast name: {}\n\
\tMiddle name: {}\n\
\tGender: {}\n\
\tBirth date: {}\n\
\tNationality: {}\n\
\tUnit: {}\n\
\tCreated date: {}\n\
\tExpiry date: {}\n\
\tNumber: {}\n"

class Passport:
    def __init__(self, first_name, last_name, middle_name,
                gen:str, birth_date, nationality) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.gen = gen
        self.birth_date = birth_date
        self.nationality = nationality

        self.unit = random.randint(1111,9999)
        self.__number = random.randint(10000000,999999999)
        self.created_date = datetime.datetime.today()

    def __str__(self) -> str:
        return f"Passport: {self.first_name} {self.last_name}"

    def _print(self):
        print(PASSPORT_INFO.format(self.first_name, self.last_name,
                    self.middle_name, self.gen, self.birth_date,
                    self.nationality, self.unit,  
                    self.created_date.strftime("%d-%m-%Y"), "EXP", 
                    self.__number))

    def get_exp_date(self):
        return self.created_date + '10Y'

class ForeignPassport(Passport):
    
    def __init__(self, first_name, last_name, middle_name, gen: str,
                birth_date, nationality):
        super().__init__(first_name, last_name, middle_name, gen, 
                birth_date, nationality)
        self.visa = []
        self.unit = random.randint(1111,9999)
        self.__number = random.randint(10000000,999999999)
        self.created_date = datetime.datetime.today()

    def _print(self):
        print(F_PASSPORT_INFO.format(self.first_name, self.last_name,
                        self.middle_name, self.gen, self.birth_date,
                        self.nationality, self.unit,  
                        self.created_date.strftime("%d-%m-%Y"), "EXP", 
                        self.__number))
        print("Visa info:")
        for item in self.visa:
            for key in item:
                print(f"\t{key} - {item[key]}")
            # print(f"\t{list(item.keys())[0]} - {list(item.values())[0]}")

    def new_visa(self, country, end_time):
        self.visa.append({country:end_time})





Bob = Passport('Bob', 'Bobik', 'Bobikov', 'M', '25.06.2000', 'USA')
Bob = Passport('Bob', 'Bobik', 'Bobikov', 'M', '25-06-2000', 'USA')

print(Bob, Bob.unit, Bob.created_date)

Bob._print()

Bob_f = ForeignPassport('Bob', 'Bobik', 'Bobikov', 'M', '25-06-2000', 'USA')
Bob_f.new_visa('China', '26-06-2022')

Bob_f._print()