# Keypoints to note down:
# we'll imagine our array into 2 parts: sorted and unsorted
# initially we'll assume all elements are sorted
# then we'll loop & check which element is smallest, and put it at 0th index (and that will be our sorted array) by swapping with the element at 0th index and this will goes on!

# Time-Complexity: Best, Worst, Average → O(n²)
# Space-Complexity: O(1)

arr = [8, 3, 5, 9, 2, 4]

def selection_sort(arr):
    pass