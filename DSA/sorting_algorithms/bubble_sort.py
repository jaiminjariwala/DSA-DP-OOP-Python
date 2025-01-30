# Keys to note down:
# Concept: Repeatedly swap adjacent elements if they are in the wrong order
# Time-Complexity: Best-Case: O(n) - already sorted
#                  Worst-Case: O(n²)
# Space-Complexity: O(1)

def bubble_sort(arr):
    is_swap = False
    number_of_elements = len(arr)

    for i in range(number_of_elements-1):   # this loop will run iterations
        for j in range(number_of_elements-i-1): # for comparisons

            # when a swap occurs, the "is_swap" flag is enabled
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j] # swapping
                is_swap = True

        if not is_swap:
            break   # Optimization: stop execution of further iterations if array is already sorted
    
    return arr

arr = [8, 3, 5, 9, 2, 4]
print(f"Sorted array using Bubble Sort is: {bubble_sort(arr)}")