# @staticmethod: This decorator converts a regular method into a static method.
# static methods in python are methods that belong to a class, rather than an instance of the class. They do not receive an automatic "self" or "cls" parameter.

# @classmethod: This decorator converts a method into a class method, which receives the class as its first parameter instead of an instance.

# example-1: @staticmethod
class MathUtils:
    @staticmethod
    def add(x, y):
        return x + y
    
result = MathUtils.add(2, 3)
print(result)

# in the above example, "add" is a static method. We can call it directly using the class name, without creating an instance of the class.






# example-2: @staticmethod and @classmethod
class MyClass:
    class_variable = "I am a class variable"

    def __init__(self, value):
        self.value = value      # this is an instance variable

    @staticmethod
    def static_method():
        """
        This method doesn't access class or instance variable.
        """
        print(f"I am a static method, I don't need the class or instance.")

    @classmethod
    def class_method(cls):
        """
        This method can access class variables but not the instance variables.
        """
        print(f"I am a class method, I can access class variables. For instance: {cls.class_variable}")
        
obj = MyClass(23)

MyClass.static_method() # no need for an instance, when calling a static method
obj.static_method() # can also be called on an instance, but doesn't use it.

MyClass.class_method()  # works on the class itself.
obj.class_method() # works on an instance but still operates on the class.






# example-3
class Temperature:
    celsius_to_fahrenheit_factor = 1.8  # this is a class variable

    def __init__(self, celsius):
        self.celsius = celsius  # this is an instance variable

    @staticmethod   # static methods can be used as a general utility function.
    def convert_celsius_to_fahrenheit(celsius):
        """
        Convert celsius to fahrenheit using a formula
        """
        return (celsius * 1.8) + 32 # doesn't use class or instance variables
    
    @classmethod
    def from_fahrenheit(cls, fahrenheit):   # cls parameter is used to access class variable and it refers to the class itself!
        """
        Alternative constructor: Create an instance from Fahrenheit
        """
        celsius = (fahrenheit - 32) / cls.celsius_to_fahrenheit_factor
        return cls(celsius) # returns a new instance of temperature by calling the class constructor "__init__"
    

print(Temperature.convert_celsius_to_fahrenheit(23))    # static method

temp_obj = Temperature(23)
print(temp_obj.celsius)