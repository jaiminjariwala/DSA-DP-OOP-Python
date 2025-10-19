# Maximum Contiguous Subarray Sum(MCSS) or Maximum Value Contiguous Sum(MVCS) - Dp Approach O(n)
# the idea is to maintain a running sum of the maximum subarray that ends at each position in the array.
# the sum is updated at each step based on whether adding the current element increases or decreases the sum.
# keep track of global maximum sum encountered so far.

from typing import List
def max_subarray_sum_dp(arr: List[int]) -> int:
    """
    Dynamic Programming approach to find the maximum contiguous subarray sum.
    """
    max_sum = float("-inf")
    current_sum = 0

    for num in arr:
        print(f"num: {num}, current_sum: {current_sum}, max_sum: {max_sum}")
        current_sum = max(num, current_sum + num) # decide whether to add the current number to the existing subarray or start a new subarray with the current number
        max_sum = max(max_sum, current_sum) # update the global maximum sum if the current sum is greater
    return max_sum

arr = [-2,1,-3,4,-1,2,1,-5,4]
print(max_subarray_sum_dp(arr))