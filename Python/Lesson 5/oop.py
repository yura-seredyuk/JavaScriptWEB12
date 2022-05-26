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

#     @staticlass_mutableethod
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



# class Singletone:
#     obj = None

#     def __new__(cls, *arg, **kwarg):
#         # print('NEW', type(cls))
#         if cls.obj is None:
#             cls.obj = object.__new__(cls, *arg, **kwarg)
#         return cls.obj

#     def __init__(self) -> None:
#         print('INIT', type(self))
#         self.id = 2

# s1 = Singletone()
# s2 = Singletone()

# print(id(s1), id(s2))


# s3 = Singletone()
# s1.id = 5
# print(s3.id, s2.id)


class MyClass:
    class_mutable = []
    class_inmutable = 'cl_inm'

    def __init__(self) -> None:
        self.instance_mutable = []
        self.instance_inmutable = 'inst_inm'
        self.__some = 'text'

a = MyClass()

print('a1', a.class_mutable, a.class_inmutable, a.instance_mutable, a.instance_inmutable)

b = MyClass()

b.class_mutable.append(1)
b.class_inmutable = 'new_class_mutable'
b.instance_mutable.append(2)
b.instance_inmutable = 'new_instance_mutable'
print('a2', a.class_mutable, a.class_inmutable, a.instance_mutable, a.instance_inmutable)
print('b ', b.class_mutable, b.class_inmutable, b.instance_mutable, b.instance_inmutable)

c = MyClass()
c.instance_mutable.append(5)
print('c ', c.class_mutable, c.class_inmutable, c.instance_mutable, c.instance_inmutable)
# mutable: list, dict, set
# inmuteble: frozenset, tuple, str, int, float, bool, NoneType