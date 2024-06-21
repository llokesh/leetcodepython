"""Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true"""

# Bruteforce O(n2)
def containsDuplicate_1(nums: list[int]) -> bool:
    """Returns true if the array nums contains duplicate elements by brute force approach

    Args:
        nums (list[int]): list of numbers

    Returns:
        bool: True if there is a duplicate element else False
    """
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                return True

        return False
    
# Sets O(NlogN)
def containsDuplicate_2(nums: list[int]) -> bool:
    """Returns true if the array nums contains duplicate elements by comparing length of array list and length of sets converted to array list

    Args:
        nums (list[int]): list of numbers

    Returns:
        bool: True if there is a duplicate element else False
    """
    set_list = list(set(nums))
    if len(nums) > len(set_list):
        return True
    return False


# Sort O(NlogN)
def containsDuplicate_3(nums: list[int]) -> bool:
    """Returns true if the array nums contains duplicate elements by comparing length of array list and length of sets converted to array list

    Args:
        nums (list[int]): list of numbers

    Returns:
        bool: True if there is a duplicate element else False
    """
    sorted_num = sorted(nums)
    for next in range(1, len(sorted_num)):
        if sorted_num[next] == sorted_num[next-1]:
            return True        
        else:
            return False
        

# Hash set O(N)
def containsDuplicate_4(nums: list[int]) -> bool:
    """Returns true if the array nums contains duplicate elements by storing the unique elements in hash set 

    Args:
        nums (list[int]): list of numbers

    Returns:
        bool: True if there is a duplicate element else False
    """
    hashSet = set()
    for n in nums:
        if n in hashSet:
            return True
        hashSet.add(n)
    return False



print(containsDuplicate_1([1,2,3,1]))
print(containsDuplicate_2([1,2,3,1]))
print(containsDuplicate_3([1,2,3,1]))
print(containsDuplicate_4([1,2,3,1]))
