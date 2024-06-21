"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
"""
# Built in methods
def isPalindrome_1(s: str) -> bool:
    for i in s:
        if not i.isalnum():
            s = s.replace(i, '')

    return s.lower() == s[::-1].lower()


def isAlphaNum(c: str) -> bool:
    return (ord('A')<= ord(c) <= ord('Z') or 
     ord('a')<= ord(c) <= ord('z') or 
     ord('0')<= ord(c) <= ord('9'))

    
# 2 pointer methods
def isPalindrome_2(s: str) -> bool:
    L = 0
    R = len(s) - 1
    while L < R:
        while L < R and not isAlphaNum(s[L]):
            L += 1
        while R > L and not isAlphaNum(s[R]):
            R -= 1
        if s[L].lower() != s[R].lower():
            return False
        L += 1
        R -= 1
        
    return True
                
    
print(isPalindrome_1("A man, a plan, a canal: Panama"))
print(isPalindrome_2("A man, a plan, a canal: Panama"))
        