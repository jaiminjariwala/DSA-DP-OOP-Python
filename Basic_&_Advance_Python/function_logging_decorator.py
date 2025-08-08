import datetime

def log_with_timestamp(func):
    def wrapper(*args, **kwargs):

        #logging before the actual function call
        #strftime is "string format time"
        timestamp=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"\n[{timestamp}] Called function: {func.__name__} with args: {args}, kwargs: {kwargs}\n")

        return func(*args, *kwargs)
    
    return wrapper

@log_with_timestamp
def greet(name):
    print(f"Hello, {name}!")

greet("Jaimin")