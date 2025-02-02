# public, private, protected
class BankAccount:
    def __init__(self, name, balance):
        self.name = name    # public
        self._account_number = 12345    # protected
        self.__balance = balance    # private

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit must be positive integer!")

    def get_balance(self):
        return self.__balance
    
account = BankAccount("John", 1000)
print(account.name)     # public variable
print(account._account_number)  # it's accessible in python, not strictly enforced as in other languages like c++ and java, but here it should be considered protected!

# print(account.__balance)  # this will thow "AttributeError (Private)" error!
 
account.deposit(8000)
print(account.get_balance())    # access private data via method!




# ================================================




# abstract class and methods
from abc import ABC, abstractmethod

class Vehicle(ABC): # Abstract Base Class
    @abstractmethod
    def fuel_type(self):
        pass

class Car(Vehicle):
    def fuel_type(self):
        return "petrol"

class ElectricCar(Vehicle):
    def fuel_type(self):
        return "electric"

c = Car()
print(c.fuel_type())    # petrol
 
e = ElectricCar()
print(e.fuel_type())    # electric