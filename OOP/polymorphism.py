# function overloading: 1. using "default" arguments
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Johnny")
greet("Miracle", "Hi")
# in above function parameter, greeting has a default value of "Hello". We can call the function with or without providing a greeting.



# function overloading: 2. using variable-length arguments (*args and **kwargs)
# *args: allows us to pass an arbitrary number of positional arguments to a function.
def sum_numbers(*args):
    print("Arguments are: ", *args)
    total=0
    for num in args:
        total = total + num
    return total

result1 = sum_numbers(1, 2, 3)
result2 = sum_numbers(20, 40)


# =============================================



# method overriding:
class Parent:
    def show(self):
        print("Parent Method")

class Child(Parent):
    def show(self): # overriding the parent method
        print("Child Method")

c = Child()
c.show()    # Output: Child Method
