# example-1: logging decorator
def log_function_calls(func):
    """
    Logs the name of the function and its arguments before and after exectuion!
    """
    def wrapper(*args, **kwargs):
        print(f"Function Name: {func.__name__}")
        print(f"Function Args: {args}")
        print(f"Function Kwargs: {kwargs}")
        print(f"Function returns... {func(*args, **kwargs)}")
        print("="*20)
    
    return wrapper

@log_function_calls
def add (x, y):
    return x + y

@log_function_calls
def greet (name):
    return f"Hello, {name}!"


add(2, 3)
greet("Jaimin")