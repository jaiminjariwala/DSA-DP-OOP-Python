# Given a sorted array...
# Input: [1, 2, 3, 4, 5] [5, 2, 3, 4, 1]
# Output: [5, 4, 3, 2, 1]

def reverse_array(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr

print(reverse_array([1, 2, 3, 4, 5]))