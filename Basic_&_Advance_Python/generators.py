def my_generator_function():
    """A simple generator function"""
    for i in range(5):
        yield i    # the yield keyword pauses the function and returns the current value of i

for number in my_generator_function():
    print(number)
    
    
# another example
def count_up_to(n):
    i=0
    while i<n:
        yield i
        i+=1
    
for number in count_up_to(10):
    print(number)