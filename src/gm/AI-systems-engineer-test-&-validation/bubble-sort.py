"""
Bubble Sort
Problem:
Given an array of integers nums, sort the array in ascending order using the Bubble Sort algorithm.

You must write an algorithm with O(n²) runtime complexity.

Bubble Sort repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.
After each pass, the largest unsorted element "bubbles" up to its correct position.
nums = [5, 3, 8, 4, 2]
print(bubble_sort(nums))
"""

def bubble_sort(nums):
    n = len(nums)

    for i in range(n):
        swapped = False

        for j in range(0, n-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] =  nums[j+1], nums[j]
                swapped = True

        if not swapped:
            break

    return nums

nums = [5, 1, 4, 2, 5]
print(bubble_sort(nums))