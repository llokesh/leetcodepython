"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.
"""
# In built index method
def strStr_1(haystack: str, needle: str) -> int:
    """Finds the first occurance using the in built index method python

    Args:
        haystack (str): String
        needle (str): sub string

    Returns:
        int: index of the first occurance of the sub string inside a string else returns -1
    """
    if needle in haystack:
        return haystack.index(needle)       
    else:
        return -1

# Brute force O(NxM)
def strStr(haystack: str, needle: str) -> int:
    """Finds the first occurance using the in built index method python
    Uses brute force method to traverse through the haystack (minus the length of the needle - no need to traverse all the way towards the end of the needle)

    Args:
        haystack (str): String
        needle (str): sub string

    Returns:
        int: index of the first occurance of the sub string inside a string else returns -1
    """
    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i: i+len(needle)] == needle:
            return i

    return -1