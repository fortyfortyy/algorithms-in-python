"""
Function that takes in a non-empty string and that returns a boolean representing whether the string is a palindrome.
A palindrome is defined as a string that's written the same forward and backward.

Sample Input               |        Sample Output
string = 'abcdcba'         |            true
"""

# O(n) time | O(1) space
def is_palindrome(string):
    return string == string[::-1]


print(is_palindrome('abcdcba' ))