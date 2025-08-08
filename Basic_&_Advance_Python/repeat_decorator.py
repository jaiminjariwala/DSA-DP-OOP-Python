#call a function multiple times automatically

def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"*args: {args} and **kwargs: {kwargs}")
            for _ in range(3):
                func(*args, **kwargs)
        return wrapper
    return decorator


@repeat(3)
def greet(name):
    print(f"Hello {name}")


greet(name="Jaimin")
