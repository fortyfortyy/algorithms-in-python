"""
Function that takes in a non-empty array of integers that are sorted in ascending order and returns a new array of the
same lenght with the squares of the original integers also sorted in ascending order.

Sample input:                                              |       Sample Output:
coins = [-50, -13, -2, -1, 0, 0, 1, 1, 2, 3, 19, 20]       |       [0, 0, 1, 1, 1, 4, 4, 9, 169, 361, 400, 2500]
"""

# O(n) time | O(1) space - where n is the lenght of the input array
def sorted_squared_array(array):
    return sorted(list(map(lambda x: x * x, array)))


arr = [-50, -13, -2, -1, 0, 0, 1, 1, 2, 3, 19, 20]
print(sorted_squared_array(arr))