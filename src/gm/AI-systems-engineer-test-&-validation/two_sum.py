"""
Given an array of integers nums and an integer target,
return the indices of the two numbers such that they add up to target.
"""
def two_sum(nums, target):
    n = len(nums)
    if n < 2:
        return -1, -1
    
    for i in range(n):
        for j in range(i+1, n):
            if (nums[i] + nums[j]) == target:
                return i, j
            
    return -1, -1

nums = [2, 7, 11, 15]
target = 13

print(two_sum(nums, target))