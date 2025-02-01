# here there applies a concept of mutable and immutable data types in python and how it influences the way they are passed to functions!


# =======================================================


# CALL BY VALUE:
# in python, data-types like "int", "float", "str", "tuple", "bool" are considered immutable. This means their values cannot be changed after they are created.
# When you pass an immutable object (like an integer) to a function, a copy of the value is effectively passed. Any modifications made to that value within the function do not affect the original variable outside the function.

def modify_number(num: int):
    num = num + 10
    print(f"Inside function: {num}")

num = 5
modify_number(num)  # when called, a copy of 5 is passed to the function.
print("Outside function:", num)


# =======================================================



# CALL BY REFERENCE:
# data types like "list", "dict", "set" are mutable. This means their contents can be changed after they are created (e.g., adding elements to a list, modifying dictionary values).

from typing import List

def modify_list(my_list: List[int]):
    my_list.append(4)

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)

# =======================================================