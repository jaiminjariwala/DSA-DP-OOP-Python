# functions that modify other functions are called decorators

# decorate add function
# so we'll create a function that takes in a function as an argument and decorates it!
# wrapper is the inner function that modifies the behaviour of the "func -> add"
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        result = func(*args, *kwargs)
        print(f"Result: {result}")
        return result
    return wrapper


# we will decorate add(x, y) function
@my_decorator
def add(x, y):
    return x + y

result = add(2, 3)