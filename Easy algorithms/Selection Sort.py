"""
Function that takes in an array of integers and returns a sorted version of that array.
The algorithm being used is: Selection Sort


Sample Input                    |       Sample Output
array = [8, 5, 2, 9, 6, 3]      |      [2, 3, 5, 6, 8, 9]
"""

# O(n^2) time | O(1) space - where n is the length of the input array
def selection_sort(array):
    pointer = 0

    while pointer < len(array):
        min_idx = pointer
        for idx in range(pointer, len(array)):
            if array[min_idx] > array[idx]:
                min_idx = idx

        array[pointer], array[min_idx] = array[min_idx], array[pointer]
        pointer += 1

    return array


print(selection_sort([8, 5, 2, 9, 6, 3]))