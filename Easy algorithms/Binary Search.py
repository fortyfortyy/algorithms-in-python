"""
Function that takes in a sorted array of integers as well as a target integer.
The function use the Binary Search algorithm to determine if the target integer is contained in the array
and returns its index if it is, otherwise - 1.

Sample input:                               |       Sample Output:
array = [0, 1, 21, 33, 45, 61, 71, 73]      |            3
target = 33                                 |
"""


def binary_search(array, target):
    return binary_search_helper(array, target, 0, len(array) - 1)

# # O(log(n)) time | O(log(n)) space
# def binary_search_helper(array, target, left, right):
#     if left > right:
#         return -1
#
#     middle = (left + right) // 2
#     potential_match = array[middle]
#     if potential_match == target:
#         return middle
#     elif potential_match > target:
#         return binary_search_helper(array, target, left, middle - 1)
#     else:
#         return binary_search_helper(array, target, middle - 1, right)


# # O(log(n)) time | O(1) space (faster algorithm)
def binary_search_helper(array, target, left, right):
    while left <= right:
        middle = (right + left) // 2
        potential_match = array[middle]

        if potential_match == target:
            return middle
        elif potential_match > target:
            right = middle - 1
        else:
            left = middle + 1

    return -1


array = [0, 1, 21, 33, 45, 61, 71, 73]
target = 45
print(binary_search(array,target))