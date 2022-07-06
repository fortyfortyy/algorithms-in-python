"""
Function that takes in an array of integers abd returns a sorted version of that array.
The name of algorithm being used is: Bubble Sort

Sample Input                    |       Sample Output
array = [8, 5, 2, 9, 6, 3]      |      [2, 3, 5, 5 6, 8, 9]
"""

# Best: O(n) time | O(1) space - where n is the length of the input array
# Average: O(n^2) time | O(1) space - where n is the length of the input array
# Worst: O(n^2) time | O(1) space - where n is the length of the input array
def bubble_sort(array: [int]) -> []:
    lenth_array = len(array)
    while lenth_array > 0:
        for idx in range(len(array) - 1):
            if array[idx] > array[idx + 1]:
                array[idx], array[idx + 1] = array[idx + 1], array[idx]

        lenth_array -= 1

    return array


print(bubble_sort([8, 5, 2, 9, 6, 3]))