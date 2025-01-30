# Key to Note down:
# When a function calls itself recursively, it pauses execution at that point and starts a new instance of itself. Each call gets its "OWN MEMORY SPACE" on the call stack.

# So each recursive call remembers its own copy of array, and values like "left_half" and "right_half" belong to different calls, not the same one.

# merge_sort([8,3,5]) and merge_sort([3,5]) are separate function calls. The have different local variables "arr", "left_half" and "right_half"

def merge_sort(arr):
    print("Entering merge sort with an array:", arr)   # to see what's happening

    # base case: if the array has one or fewer elements, it's already sorted, so it will returns the array as it is!
    if len(arr) <= 1:
        print("Base case reached:", arr)
        return arr
    
    # divide the array by splitting into 2 halves using mid!
    mid = len(arr) // 2
    print("Mid is:", mid)

    left_half = merge_sort(arr[:mid])
    print("Returned from left_half is:", left_half)     # when left_half is done

    print("\n====== Going back to the call where it was paused ======")
    right_half = merge_sort(arr[mid:])
    print("Returned from right_half is:", right_half)   # when right_half is done

    return merge(left_half, right_half)


def merge(left_half, right_half):
    sorted_array = []
    i = j = 0
    # i is the index of left_half, j is the index of right_half array

    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            sorted_array.append(left_half[i])
            i+=1
        else:
            sorted_array.append(right_half[j])
            j+=1

    # Once the while loop ends, one of the lists may still have remaining elements.Since left_half and right_half were already sorted individually, we can simply add all remaining elements without further comparison.
    sorted_array.extend(left_half[i:])
    sorted_array.extend(right_half[j:])

    # extend() method adds all elements from another list unless append which adds a single element at a time.
    # Instead of adding b as a single list ([1, 2, 3, [4, 5, 6]]), it flattens b into a.

    return sorted_array


arr = [8, 3, 5, 9, 2, 4]
print(f"Final sorted array: {merge_sort(arr)}")


# Visualization of the call stack:

# merge_sort([8, 3, 5, 9, 2, 4])
#  ├── merge_sort([8, 3, 5])
#  │    ├── merge_sort([8])  → Returns [8]
#  │    ├── merge_sort([3, 5])
#  │    │    ├── merge_sort([3])  → Returns [3]
#  │    │    ├── merge_sort([5])  → Returns [5]
#  │    │    └── merge([3], [5])  → Returns [3, 5]
#  │    └── merge([8], [3, 5])  → Returns [3, 5, 8]
#  ├── merge_sort([9, 2, 4])  (Executes next)



# in simple terms...
# Think of recursion like a stack of unfinished tasks.
# each recursive call waits until the smaller subproblems finish and resumes exactly where it left off.