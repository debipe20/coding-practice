"""
## Problem

Given an array of integers nums and a target value target, search for the target in the array.
Return the index if found; otherwise, return -1.

You must write an algorithm with O(n) runtime complexity.

Input: nums = [-1, 0, 3, 5, 9, 12], target = 9
Output:4

Input: nums = [-1, 0, 3, 5, 9, 12], target = 2
Output:-1

"""


def linear_search(nums, target):
    for i in range(len(nums)):
        if nums[i] ==  target:
            return i
        
    return -1

def linear_search(nums, target):
    for index, value in enumerate(nums):
        if value == target:
            return index
    return -1
