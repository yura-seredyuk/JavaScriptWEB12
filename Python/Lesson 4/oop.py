# абстракція
# наслідування
# інкапсуляція
# поліморфізм


#               фігура
#                   побудова():pass
#                   line_color
#                   line_type
#                   fill_style

# коло              квадрат         трикутник
#   побудова()          побудова()      побудова()

# incapsulation
#  value - public
#  _value - protected
#  __value - private


class Person:
    DNA = 'Human'

    # def __init__(self, name = 'no name', age = 0):
    #     self.name = name
    #     self.age = age
    def __init__(self, name = 'no name', age = 0):
        self._name = name
        self.__age = age

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



Bob = Person('Bob', 30)
Bob.description()
Rob = Person('Rob', 20)
Rob.DNA = 'Monkey'
Rob.description()
# print(Bob.age, Bob.name, Bob.DNA)
# print(Rob.age, Rob.name, Rob.DNA)
Bob.set_age(32)
print(Bob._name, Bob.get_age())
Bob.age = 40
print(Bob._name, Bob.age)
# print(Rob._age, Rob.name, Rob.DNA)
