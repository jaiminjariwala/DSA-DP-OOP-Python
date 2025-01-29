# works only on sorted arrays
# uses divide & conquer to eliminate half of the elements at each step
# instead of searching sequentially(like linear search), it compares with the middle element and decides to search in left or right half.

# time complexity: best-case => O(1), worst/average-case => O(log(n))


def binary_search(arr, target):
    low, high = 0, arr[-1]
    

    while low <= high:
        mid = (low + high) // 2 # find middle index

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1   # search right half
        else:
            high = mid - 1  # search left half

    return -1


arr = [2,3,4,5,6,7,8,9]
target = 3
print(f"{target} is located at index location: {binary_search(arr, target)}")