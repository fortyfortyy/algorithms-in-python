"""
Function that takes in an array of integers and returns a boolean representing whether the array is monotonic.

An array is said to be monotonic if its elements, from left to right, are enitrely non-increasing or enitrely
non-decreasing.
Non-increasing elements aren't necessarily exclusively decreasing; they simply don't increase. Similarly,
non-decreasing elements aren't necessarily exclusively increasing; they don't decrease.

An empty arrays and arrays of one element are monotonic.

        Sample Input                                        |       Sample Output
array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]    |           true
"""

# O(n) time | O(1) space where n is the lenght of array

def is_monotonic(array):
    if len(array) < 2:
        return True

    nonIcreasing = True
    nonDecreasing = True
    for idx in range(1, len(array)):
        if array[idx - 1] > array[idx]:
            nonIcreasing = False

        elif array[idx - 1] < array[idx]:
            nonDecreasing = False

    return nonIcreasing or nonDecreasing


print(is_monotonic([-1, -5, -10, -1100, -1100, -1101, -1102, -9001]))