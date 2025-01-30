def runningSum_optimized(nums):
    for i in range(1, len(nums)):  # Single loop O(n)
        nums[i] += nums[i-1]  # Modify nums in-place
    return nums

# Example
nums = [1, 2, 3, 4]
print(runningSum_optimized(nums))  # Output: [1, 3, 6, 10]
