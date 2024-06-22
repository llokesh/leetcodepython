"""
Given an integer x, return true if x is a 
palindrome
, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1
 

Follow up: Could you solve it without converting the integer to a string?
"""
def isPalindrome_1(x: int) -> bool:
    """Finding the palindrome of a number by converting it into string and then list

    Args:
        x (int): number

    Returns:
        bool: True or False
    """
    
    strx = str(x)
    listx = list(strx)

    if(listx[::-1] == listx):
        return True
    else:
        return False
    
def isPalindrome_2(x: int) -> bool:
    """Finding the palindrome of a number by mathematical operations

    Args:
        x (int): number

    Returns:
        bool: True or False
    """
    temp = x
    rev = 0
    while (x > 0):
        mod = x%10
        rev = rev*10 + mod
        x = x//10

    if(temp == rev):
        return True
    else:
        return False

        
print(isPalindrome_1(12321))
print(isPalindrome_2(12321))