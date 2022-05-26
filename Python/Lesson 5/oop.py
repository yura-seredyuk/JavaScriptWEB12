# # inheritance / polimorphism

# class Ss:
#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age

#     def info(self):
#         pass

#     def voice(self):
#         pass

# class Animal(Ss):
#     def info(self):
#         print(f"My name is {self.name}. I am {self.age}.")

# class Dog(Animal):
#     def voice(self):
#         print('Woof!!!')

# class Cat(Animal):
#     def voice(self):
#         print('Meow!!!')

# cat = Cat('Boris', 2)
# dog = Dog('Patron', 3)

# cat.info()
# cat.voice()
# dog.info()
# dog.voice()


# multiple inheritance

# class A:
#     def m_1(self):
#         return '(From A m_1)'

#     def m_2(self):
#         return '(From A m_2)'

# class B:
#     def m_2(self):
#         return '(From B m_2)'

#     def m_3(self):
#         return '(From B m_3)'

# class C(A, B):
#     pass

# c = C()
# print(c.m_1(), c.m_2(), c.m_3())



# class Door:

#     color = "black"
#     material = "wood"

#     def __init__(self, number, status = 'close') -> None:
#         self.number = number
#         self.status = status

#     def open(self):
#         self.status = 'open'

#     def close(self):
#         self.status = 'close'

# class SequredDoor(Door):
    
#     material = "iron"

#     def __init__(self, number, status='close', locked = True) -> None:
#         # super().__init__(number, status = status)
#         Door.__init__(self, number, status)
#         self.locked = locked

#     def open(self, key:bool):
#         self.locked = not key
#         if not self.locked:
#             self.status = 'open'

#     def close(self, key:bool):
#         self.locked = key
#         if self.locked:
#             self.status = 'close'

# door = Door(1)
# door.color = 'red'
# Door.color = 'white'
# door.open()
# door.close()
# print('Door1 ', door.status)
# print(door.color)
# print(door.material)


# s_door = SequredDoor(2)
# s_door.open(True)
# s_door.close(True)
# print('Door2 ', s_door.status)
# print(s_door.color)
# print(s_door.material)


# print(door.__dict__)
# print(s_door.__dict__)

# print(door.__dir__())
# x = 5
# print(x.__dir__())


# class Shape:
#     color = "red"

#     def __init__(self, name):
#         self.name = name

#     def area(self):
#         pass

#     def description(self):
#         return "Unknown figure"

#     def __str__(self) -> str:
#         return "Instance of " + self.name

#     def __repr__(self) -> str:
#         return "Figure: " + self.name

#     def __del__(self):
#         print("Figure: " + self.name + " was remowed!")
    
# class Square(Shape):
#     def __init__(self, side):
#         super().__init__('Square')
#         self.side = side

#     @classmethod
#     def fig(cls,color:str):
#         cls.color = color
#         return "Classmethod " + cls.color

#     @staticmethod
#     def func(x):
#         return f"This is a {x}"

#     def description(self):
#         return 'This is a ' + self.name

#     def area(self):
#         return self.side ** 2

#     def f():
#         pass

    


# squre = Square(4)
# # del squre
# print(squre)
# print(squre.fig('yellow'))
# print(squre.func(100))
# print(8)
 