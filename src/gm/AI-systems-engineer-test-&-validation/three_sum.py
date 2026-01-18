"""
Given an array of integers nums and an integer target, 
determine whether there exist three different numbers in the array such that their sum equals target.
"""

def three_sum(nums, target):
    nums.sort()
    n = len(nums)
    result = []

    for i in range(n - 2):
        if i >0  and nums[i] == nums[i-1]:
            continue
        left = i + 1
        right = n - 1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]

            if current_sum == target:
                result.append([nums[i], nums[left], nums[right]])

                left += 1
                right -= 1

                # Skip duplicates
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
                
            elif current_sum < target:
                left += 1
            else:
                right -= 1

    return result

nums = [3, 5, 8, 2, 4, 7] 
target = 13

print(three_sum(nums, target))