# 1. works well with unsorted arrays
# 2. used when the dataset is small

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            print(f"Your element is present at an index location: {i}")    
        
    return -1   # return -1 if not found


arr = [5, 6, 7, 3, 4, 8]
target = 8

linear_search(arr, target)