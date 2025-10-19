# Maximum Contiguous Subarray Sum(MCSS) or Maximum Value Contiguous Sum(MVCS) - Better Approach O(n^2)


# in better approach, instead of recalculating the sum of each subarray from scratch, we compute the sum incrementally as we extend the subarray from the starting point.


from typing import List
def max_contiguous_subarray_sum_better(arr: List[int]) -> int:
    """
    Better approach to find the maximum contiguous subarray sum.
    """
    n = len(arr)
    max_sum = float("-inf")

    for start in range(n):
        current_sum = 0
        for end in range(start, n):
            current_sum += arr[end]
            print(f"  Adding arr[{end}] = {arr[end]} to current_sum: {current_sum}")
            max_sum = max(max_sum, current_sum)
            print(f"  Current subarray sum from index {start} to {end}: {current_sum}, Max sum so far: {max_sum}")
    return max_sum

arr = [-2,1,-3,4,-1,2,1,-5,4]
print(max_contiguous_subarray_sum_better(arr))