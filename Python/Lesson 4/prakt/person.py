# def lines(func):
#     def wrapper():
#         print("*"*20)
#         func()
#         print("*"*20)
#     return wrapper()

class Person:
    DNA = 'Human'

    def __init__(self, name = 'no name', age = 0):
        self._name = name
        self.__age = age
        self.__address = 'n/a'

    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,age):
        if age > 0:
            self.__age = age
        else:
            print('Error!')
    
    # @lines
    def description(self):
        print("*"*20)
        print(f"| Name: {self._name}.")
        print(f"| Age: {self.__age}.")
        print(f"| Address: {self.__address}.")
        print("*"*20)


if __name__ == "__main__":
    Bob = Person('Bob', 30)
    Bob.description()