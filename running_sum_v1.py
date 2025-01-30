def runningSum_brute_force(nums):
    running_sum = []
    for i in range(len(nums)):
        total = sum(nums[:i+1])  # Recomputes sum every time
        running_sum.append(total)
    return running_sum

# Example
nums = [1, 2, 3, 4]
print(runningSum_brute_force(nums))  # Output: [1, 3, 6, 10]
