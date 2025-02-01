# Key takeaway points:


# About SELF parameter:
# self refers to the instance of the class itself, it's a reference to the object
# self.last_name -> this is called instance attribute
# the "self" tells python that "_name" belongs to the instance, not just to the method's local scope.
# when we do "person = Person("Alice", 23)", then "self" inside "__init__" refers to the "person".
# When calling methods on an instance, Python automatically passes the instance as the first argument. So "person.some_method()" is equivalent to "Person.some_method(person)" if called directly on the class.
# "self" is equivalent to "this" in c++


# ACCESS MODIFIERS
# the single underscore (_name) before the name is a convention in python, to indicate that this attribute is "PROTECTED".
# to make an attribute truly "PRIVATE", we use doubble underscore before the name, for ex. (__age)
# by default, attributes in python are "PUBLIC"


# type hints do not enforce types at runtime, to still enforce that, we can raise TypeError
    


class Person:
    def __init__(self, name: str, age: int):
        if not isinstance(name, str):
            raise TypeError("The Name should be of type String!")
        
        if not isinstance(age, int):
            raise TypeError("The age argument value should be integer!")

        self._name = name
        self._age = age

    # getter method
    def get_age(self):
        return self._age
    
    # setter method
    def set_age(self, age): # we require the new age value!
        print(f"Previous age value was {self._age}")
        self._age = age
        print(f"Updated age value {self._age}")

p2 = Person("Mark", 42)
print(p2.get_age())

p2.set_age(29)