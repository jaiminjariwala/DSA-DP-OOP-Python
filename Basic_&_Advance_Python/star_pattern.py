"""
1.  $
    $ $
    $ $ $

2.  $ $ $
    $ $ 
    $

3.  _ _ $
    _ $ $
    $ $ $

4.  $ $ $
    _ $ $
    _ _ $

5. Hill Pattern
        # 
      # # # 
    # # # # # 
  # # # # # # # 
# # # # # # # # #

6. Reverse Hill Pattern
@ @ @ @ @ @ @ @ @ 
  @ @ @ @ @ @ @ 
    @ @ @ @ @ 
      @ @ @ 
        @ 

"""

n = int(input("Input a number: "))

# 1.
for i in range(n):
    for j in range(i+1):
        print("$", end=" ")
    print()
print()

# 2.
for i in range(n):
    for j in range(i, n):
        print("$", end=" ")
    print()
print()

# 3.
for i in range(n):
    for j in range(i, n-1):
        print(" ", end=" ")

    for j in range(i+1):
        print("$", end=" ")

    print()
print()

# 4.
for i in range(n):
    for j in range(i):
        print(" ", end=" ")

    for j in range(i, n):
        print("$", end=" ")

    print()
print()

# 5.
for i in range(n):
    for j in range(i, n-1):
        print(" ", end=" ")
    
    for j in range(i+1):
        print("#", end=" ")

    for j in range(i):
        print("#", end=" ")

    print()
print()

# 6.
for i in range(n):
    for j in range(i):
        print(" ", end=" ")
    
    for j in range(i, n):
        print("@", end=" ")
    
    for j in range(i+1, n):
        print("@", end=" ")

    print()
print()

# 7. another method to print pyramid

def print_pyramid(n):
    for i in range(n):
        spaces = " " * (n - i - 1)
        dollor = "$" * (2 * i + 1)
        print(spaces + dollor)

print_pyramid(5)
