# Insertion Sort - O(n²) Time Complexity, O(1) Space Complexity
# Keypoints to note down:
# the array is virtually split into a sorted and an unsorted part.
# values from the unsorted part are picked and placed at the correct position in the sorted part

from typing import List
def insertion_sort(arr: List[int]) -> List[int]:
    # start from the second element (index 1) as the first element is considered sorted
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        print(f"\nInserting {key} into sorted part {arr[:i]}")

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            print(f"j={j}, Shifting: {arr}")

        print(f"key={key}")
        arr[j + 1] = key
        print(f"Inserted: {arr}")

    return arr

A = [12, 11, 13, 5, 6]
print(f"\nFinal sorted array: {insertion_sort(A)}")