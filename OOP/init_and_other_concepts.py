# __init__ is a special method that automatically runs after you create an object
# technically __new__ is the actual constructor, __init__ is the initializer
# it's where we initialize the attributes of our object
# __init__ must not return anything except None
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Alice", 23)     # __init__ runs here
print(p.name, p.age)


# self is not a keyword, it's just a naming convention in python.
# it refers to the current instance of the class.
# every method in a class must take self as the first parameter (except @staticmethod)
class Example:
    def __init__(self, value):
        self.value = value

    def display(self):
        print(f"The value is {self.value}")

obj = Example(23)
obj.display()       # self refers to obj here


# a constructor can take any number of parameters after self and default parameters
class Student:
    def __init__(self, name, roll_no, course="CS"):
        self.name = name
        self.roll_no = roll_no
        self.course = course    # default value

s1 = Student("Jay", 23, "Mechatronics")
print(s1.course)


# type-hinting (just hints and not enforcement)
class Product:
    def __init__(self, name:str, price:float, in_stock:bool=True):  # we can type-hint parameters
        self.name: str = name               # we can type-hint instance attributes
        self.price: float = float
        self.in_stock: bool = in_stock

p = Product("Laptop", 999.99)


# multiple constructors (via @classmethod)
# python doesn't allow multiple __init__ overloads, but we can use alternative constructors
# cls is a conventional name used in class methods to refer to the class itself.
# in @classmethod decorator, cls is the first parameter of the method
# it is automatically passed by the python when the method is called.
class Circle:
    def __init__(self, radius:float):
        self.radius: float = radius

    @classmethod
    def from_diameter(cls, diameter:float): # cls refers to the Circle class
        return cls(diameter/2)
    
c1 = Circle(5)  # radius
c2 = Circle.from_diameter(10)   # alternative constructor


# validation inside __init__
class BankAccount:
    def __init__(self, balance:float):
        if balance<0:
            raise ValueError("Balance cannot be negative")
        self.__balance:float = balance


# using dataclasses to auto-generate __init__
# this automatically creates __init__, __repr__ and comparison methods
from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    id: int
    department: str = "General" # default-value

e = Employee("Mike", 101, "Computer Science")
print(e)


# comparison (dunder) methods in python
# python allows us to define how objects compare
class Person:
    def __init__(self, age: int):
        self.age: int = age
    
    def __eq__(self, other):
        return self.age == other.age
    
    def __lt__(self, other):
        return self.age < other.age
    
p1 = Person(25)
p2 = Person(30)

print(p1<p2)    # True
print(p1==p2)   # False


# inheritance and super()
class Animal:
    def __init__(self, name: str):
        self.name: str = name

class Dog(Animal):
    def __init__(self, name: str, breed: str):
        super().__init__(name)
        self.breed = breed