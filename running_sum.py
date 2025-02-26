def running_sum(nums):
    i = 1
    newArray = [nums[0]]
    while i < len(nums):
        newArray.append(newArray[i-1]+ nums[i])
        i += 1
    return newArray
nums = [3,1,2,10,1]
print(running_sum(nums))
