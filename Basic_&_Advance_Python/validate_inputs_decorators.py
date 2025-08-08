#validate inputs: no negative numbers

def no_negatives(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, (int, float)) and arg<0:
                raise ValueError("Negative numbers are not allowed")
        return func(*args, **kwargs)
    return wrapper

@no_negatives
def multiply(x, y):
    return x*y

print(multiply(3, 5))
print(multiply(3, -5))