"""
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105
"""

# O(N)
def containsNearDuplicate(nums: list[int], k:int) -> int:
        """Using 2 pointers method and hashSet --> Concept of sliding window

        Args:
            nums (list[int]): _description_
            k (int): _description_

        Returns:
            int: _description_
        """

        hashSet = set()
        L = 0 
        for R in range(len(nums)):
        # Check if window is too large
            if R - L  > k:
                # Remove the element on the left pointer and increment the left pointer to allow the comparison only within that specific window
                hashSet.remove(nums[L])
                L += 1
            if nums[R] in hashSet:
                return True
            else:
                hashSet.add(nums[R])
        return False

print(containsNearDuplicate([1,2,3,1],3))
print(containsNearDuplicate([1,0,1,1],1))
print(containsNearDuplicate([1,2,3,1,2,3],2))