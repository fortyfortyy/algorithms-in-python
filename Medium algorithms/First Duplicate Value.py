"""
Function that takes an array of integers between 1 and n, inclusive, where n is the length of the array.
Function returns the first integer that appears more than once (when the array is read from left to right).

In other words, out of all the integers that might occur more than once in the input array, function returns the one
whose first duplicate value has the minimum index.

If no integers appears more than once, function returns -1.

        Sample Input               |           Sample Output
array = [2, 1, 5, 2, 3, 3, 4]      |        2 // 2 is the first integer that appears more than once
"""

# O(n) time | O(1) space - where n is the length of the input array
def first_duplicate_value(array: [int]) -> int:
    for value in array:
        abs_value = abs(value)
        if array[abs_value - 1] < 0:
            return abs_value

        array[abs_value - 1] *= -1

    return -1

# O(n) time | O(n) space - where n is the length of the input array
# def first_duplicate_value(array: [int]) -> int:
#     helper = {}
#     for value in array:
#         if value not in helper:
#             helper[value] = 1
#             continue
#
#         return value
#
#     return -1


print(first_duplicate_value(array=[2, 1, 5, 2, 3, 3, 4]))   # output: 2