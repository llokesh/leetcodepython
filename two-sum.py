#Two sum
"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]"""

# Brute force O(n2)
def two_sum_1(nums: list, target: int):
    output = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if (nums[i] + nums[j] == target):
                output = [i, j]
    
    return output

# Traversing the arraylist O(N)
def two_sum_2(nums: list, target: int):
    output = []

    for i, n in enumerate(nums):
        diff = target - n
        if diff in nums and nums.index(diff) != i:
            output = [nums.index(diff), i]

    return output

# two pass Hashmap O(N)
def two_sum_3(nums: list, target: int):
    output = []
    numMap = {}

    for i, n in enumerate(nums):
        numMap[n] = i

    for i, n in enumerate(nums):
        diff = target - n
        if diff in numMap and numMap[diff] != i:
            output = [i, numMap[diff]]

    return output

# One pass Hashmap O(N)
def two_sum_4(nums: list, target: int):
    output = []
    numMap = {}

    for i, n in enumerate(nums):
        diff = target - n
        if diff in numMap:
            output = [numMap[diff], i]
        
        numMap[n] = i

    return output

print(two_sum_1([1,3,4,3], 6))
print(two_sum_2([2,7,11,15], 9))
print(two_sum_3([3,2,4], 6))
print(two_sum_4([3,3], 6))




