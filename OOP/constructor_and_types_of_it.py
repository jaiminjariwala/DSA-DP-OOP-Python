# constructor (default, parameterized, non-parameterized and copy) and destructor

class Student:
    def __init__(self, name:str = "Unknown", age:int = 18): # this is a default and parameterized constructor
        if not isinstance(name, str):
            raise TypeError("name argument should be of string type")
        if not isinstance(age, int):
            raise TypeError("age argument should be of type int")
        
        self.name = name
        self.age = age
    
    def display(self):
        print(f"Student name: {self.name}, Age: {self.age}")

    # destructor
    def __del__(self):
        print(f"Deleting object of {self.name}")

    # copy constructor
    def __copy__(self):
        """
        Creates a copy of the Student object
        """
        return Student(self.name, self.age) # call the parameterized constructor

s1 = Student()  # default constructor
s2 = Student("John", 22)    # parameterized constructor
s3 = s2.__copy__()  # copy constructor (using __copy__)
s1.display()
s2.display()

del s2  # manually calling destructor