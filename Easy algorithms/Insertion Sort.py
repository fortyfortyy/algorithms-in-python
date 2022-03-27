"""
Function that takes in an array of integers and returns a sorted version of that array.
The name of algorithm being used is: Insertion Sort

Sample Input                    |       Sample Output
array = [8, 5, 2, 9, 6, 3]      |      [2, 3, 5, 5 6, 8, 9]
"""

# Best: O(n) time | O(1) space
# Average: O(n^2) time | O(1) space
# Worst: O(n^2) time | O(1) space
def insertion_sort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
            j -= 1

    return array


print(insertion_sort([8, 5, 2, 9, 6, 3]))