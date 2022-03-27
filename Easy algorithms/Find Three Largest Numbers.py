"""
Function that takes in an array of at least three integers and without sorting the input array, returns a sorted
array of the three largest integers in the input array.
Function returns duplicate integers if necessary; for example, it returns [10, 10, 12] for an input array of [10, 5, 9, 10, 12].

Sample Input:                                           |         Sample Output:
array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]    |         [18, 141, 541]
"""

# O(n) time | O(1) space
def find_three_largest_numbers(array):
    three_largest = [None, None, None]
    for number in array:
        update_largest(three_largest, number)
    return three_largest


def update_largest(three_largest, number):
    if three_largest[2] is None or three_largest[2] < number:
        shift_and_update(three_largest, number, 2)
    elif three_largest[1] is None or three_largest[1] < number:
        shift_and_update(three_largest, number, 1)
    elif three_largest[0] is None or three_largest[0] < number:
        shift_and_update(three_largest, number, 0)


def shift_and_update(array, number, idx):
    for i in range(idx + 1):
        if i == idx:
            array[i] = number
        else:
            array[i] = array[i + 1]



print(find_three_largest_numbers([141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]))