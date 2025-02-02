# Single-level Inheritance: a child class inherits from a single parent class
# parent class
class Vehicle:
    def __init__(self, brand):
        self.brand = brand  # passing brand to the instance variable

    def get_brand(self):
        return f"Vehicle Brand: {self.brand}"
    
# child class inheriting from vehicle
class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand) # here, since super() is already referring to the parent class instance (the Vehicle object being created), we don't need to pass self explicitly.
        self.model = model

    def get_model(self):
        return f"Car Model: {self.model}"
    
car = Car("Tesla", "Model Y")
print(car.get_brand())  # Output: Vehicle Brand: Tesla
print(car.get_model())  # Output: Car Model: Model Y




# ======================================================================




# Multiple Inheritance: a child class inherits from multiple parent classes.
# parent-class-1
class Person:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        return f"Name: {self.name}"

# parent-class-2
class Employee:
    def __init__(self, company):
        self.company = company

    def show_company(self):
        return f"Company: {self.company}"
    
# child-class inheriting from both Person and Employee class
class Manager(Person, Employee):
    def __init__(self, name, company, department):
        Person.__init__(self, name)
        Employee.__init__(self, company)
        self.department = department

    def show_department(self):
        return f"Department: {self.department}"
    

mgr = Manager("John Doe", "Google", "SDE")
print(mgr.show_name())          # Output: Name: John Doe
print(mgr.show_company())       # Output: Company: Google
print(mgr.show_department())    # Output: Department: SDE




# ======================================================================



# Multilevel Inheritance: a class inherits from another class, which itself is inherited from another class!
# grandparent class
class Animal:
    def __init__(self):
        self.category = "Animal"

    def show_category(self):
        return f"Category: {self.category}"

# parent class inherting from Animal(viz. a grandparent class)
class Mammal(Animal):
    def __init__(self):
        super().__init__()
        self.type = "Mammal"

    def show_type(self):
        return f"Type: {self.type}"

# child class inheriting from Mammal(viz. a parent class)
class Dog(Mammal):
    def __init__(self, breed):
        super().__init__()
        self.breed = breed

    def show_breed(self):
        return f"Breed: {self.breed}"
    
dog = Dog("Golden Retriever")
print(dog.show_category())  # Output: Category: Animal
print(dog.show_type())      # Output: Type: Mammal
print(dog.show_breed())     # Output: Breed: Golden Retriever




# ======================================================================



# Hierarchial Inheritance: multiple child classes inherit from a single parent class.
# parent class
class BankAccount:
    def __init__(self, account_holder):
        self.account_holder = account_holder

    def show_account_holder(self):
        return f"Account holder: {self.account_holder}"

# child class 1
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, interest_rate):
        super().__init__(account_holder)
        self.interest_rate = interest_rate

    def show_interest_rate(self):
        return f"Interest rate: {self.interest_rate}%"

# child class 2
class CurrentAccount(BankAccount):
    def __init__(self, account_holder, account_balance):
        super().__init__(account_holder)
        self.account_balance = account_balance

    def show_account_balance(self):
        return f"Current account balance: ${self.account_balance}"
    
savings = SavingsAccount("Henry", 3.5)
print(savings.show_account_holder())    # Output: Account holder: Henry
print(savings.show_interest_rate())     # Output: Interest rate: 3.5%

current = CurrentAccount("George", 7900)
print(current.show_account_holder())    # Output: Account holder: George
print(current.show_account_balance())   # Output: Current account balance: $7900



# ======================================================================



# Finally there's a "Hybrid Inheritance" which is a combination of 2 or more types of inheritance!