"""
Merge Sort
Problem:
Given an array of integers nums, sort the array in ascending order using the Merge Sort algorithm.

You must write an algorithm with O(nlog(n)) runtime complexity.

Bubble Sort divide the array into two halves, recursively sort each half, and 
finally merge the sorted halves into one sorted array.

Input:  [5, 2, 4, 6, 1, 3]
Output: [1, 2, 3, 4, 5, 6]
"""

def merge_sort(nums):
    if len(nums) <=1:
        return nums
    
    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right =  merge_sort(nums[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

nums =  [5, 2, 4, 6, 1, 3]
print(merge_sort(nums))