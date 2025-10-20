# Dynamic Programming approach to find the maximum contiguous subarray sum (Simplified O(n) version)

from typing import List

def max_subarray_sum_dp_simplified(arr: List[int]) -> int:
    """
    Simplified Dynamic Programming approach to find the maximum contiguous subarray sum.
    """
    n = len(arr)
    dp = [0] * n
    print(f"Initial DP array: {dp}")
    dp[0] = arr[0]
    print(f"dp[0]: {dp[0]}")

    for i in range(1, n):
        # simplified state transition
        dp[i] = max(arr[i], dp[i-1]+arr[i])
        print(f"i: {i}, arr[i]: {arr[i]}, dp[i-1]: {dp[i-1]}, dp[i]: {dp[i]}")
    return max(dp)

arr = [-2,1,-3,4,-1,2,1,-5,4]
print(max_subarray_sum_dp_simplified(arr))