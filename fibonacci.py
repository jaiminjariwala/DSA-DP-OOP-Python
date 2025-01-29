# method-1: fibonacci using normal method
def fib_series_till_(n):
    if n <= 0:
        return "you cannot input negative number"
    elif n == 1:
        return [0]

    # initial list to hold the numbers
    fib = [0, 1]

    a, b = 0, 1

    for _ in range(2, n):
        a, b = b, a+b   # a=1, b=1
        fib.append(b)

    return fib

print(fib_series_till_(5))
    

# method-2:
def fibonacci(n):
    # initialize the first 2 numbers of the sequence
    fib_sequence = [0, 1]

    # generate next numbers upto n terms
    while len(fib_sequence) <= n:
        # next number is the sum of last 2 numbers
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

    return fib_sequence

print(fibonacci(20))

# method-3: with recursion (if user want numbers till 10)
def fibonacci_recursive(n):
    if n<=0:
        return []
    elif n==1:
        return [0]
    elif n==2:
        return [0,1]

    # recursive call
    fib_seq = fibonacci_recursive(n-1)
    fib_seq.append(fib_seq[-1]+fib_seq[-2])
    return fib_seq

print(fibonacci_recursive(10))

# method-3: with recursion (if user want to know 10th position fib value)
def fib_recursion(n):
    if n<=1:
        return n
    else:
        return fib_recursion(n-1) + fib_recursion(n-2)

user_input_num = int(input("Enter position number to know the value at that particular location in fib seq: "))    
print(f"The fib value at position {user_input_num} is {fib_recursion(user_input_num)}")