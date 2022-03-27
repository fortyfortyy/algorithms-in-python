"""
Function that takes in a string of lowercase English-alphabet letters and returns the index of the string's first
non-repeating character. The first non-repeating character is the first character in a string that occurs only once.
If the input string doesn't have any non-repeating characters, function returns -1.

Sample Input            |       Sample Output
string = "abcdcaf"      |           1    # the first non-repeating character is "b" and is found at index 1
"""

def first_non_repeating_character(string):
    letters = {}

    for letter in string:
        letters[letter] = letters.get(letter, 0) + 1

    for idx in range(len(string)):
        if letters[string[idx]] == 1:
            return idx

    return -1

print(first_non_repeating_character("abcdcaf"))