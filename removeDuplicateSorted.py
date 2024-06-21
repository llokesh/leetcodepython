"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.
Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.

 

Example 1:

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
 

Constraints:

1 <= nums.length <= 3 * 104
-100 <= nums[i] <= 100
nums is sorted in non-decreasing order.
"""

# Sets (NlogN)
def removeDuplicates_1(nums: list[int]) -> int:
    """Removes duplicates by using temporary variable to store the unique list of numbers and replacing the original list with the temporary variable
    And sorting it

    Args:
        nums (list[int]): list of numbers

    Returns:
        int: length of the unique list
    """

    unique_list = list(set(nums))
    nums[:] = unique_list

    nums.sort()
    return len(nums)


# Two pointers O(N)
def removeDuplicates_2(nums: list[int]) -> int:
    """Using the concept of 2 pointers to remove the duplicates in the sorted list

    Args:
        nums (list[int]): list of numbers

    Returns:
        int: length of the unique list
    """

    # Initialize a pointer L at the beginning of the array
    L = 1

    # Iterate through the array starting from the second element (R = 1)
    for R in range(1, len(nums)):
        # If the current element is different from the previous element
        if nums[R] != nums[R-1]:
            # Update the current position (i) with the unique element (nums[j])
            nums[L] = nums[R]
            # Increment i to move to the next unique element
            L += 1

    # Return the length of the modified array (i + 1)
    return L

print(removeDuplicates_1([1,1,2]))
print(removeDuplicates_2([1,1,2]))