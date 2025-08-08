# measure how long a function takes to execute

import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):

        start=time.time()
        result=func(*args, **kwargs)
        end=time.time()

        print(f"\n'{func.__name__}' function took {end-start:.5f} seconds to execute\n")
        return result
    return wrapper

@timing_decorator
def slow_add(a, b):
    time.sleep(1)
    return a+b

slow_add(3, 4)