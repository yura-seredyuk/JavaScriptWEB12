

class Person:
    DNA = 'Human'

    def __init__(self, name = 'no name', age = 0):
        self._name = name
        self.__age = age
        self.__address = 'n/a'

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,age):
        if age > 0:
            self.__age = age
        else:
            print('Error!')

    def description(self):
        print(f"\tName: {self._name}, age: {self.__age}.")