# Maximum Contiguous Subarray Sum(MCSS) or Maximum Value Contiguous Sum(MVCS) - Brute Force Approach O(n^3)


# in brute force approach we will generate all possible subarrays and calculate their sum.
# this approach checks every possible pair of start and end indices of subarrays and computes their sums.
# the time complexity is O(n^3) because we have to consider every subarray, and for each subarray, we are calculating the sum, which takes O(n) time.

from typing import List
def max_contiguous_subarray_sum_brute_force(arr: List[int]) -> int:
    """
    Brute Force approach to find the maximum contiguous subarray sum.
    """
    n = len(arr)
    max_sum = float("-inf")

    # generate all possible subarrays
    for start in range(n):
        print(f"Starting new subarray at index {start}")
        for end in range(start, n):
            print(f"  Considering subarray from index {start} to {end}")
            current_sum = 0
            # calculate the sum of subarray from start to end
            for k in range(start, end + 1):
                current_sum += arr[k]
                print(f"    Adding arr[{k}] = {arr[k]} to current_sum: {current_sum}")
            max_sum = max(max_sum, current_sum)
    
            print(f"  Current subarray sum: {current_sum}, Max sum so far: {max_sum}")
    return max_sum

arr = [-2,1,-3,4,-1,2,1,-5,4]
print(max_contiguous_subarray_sum_brute_force(arr))