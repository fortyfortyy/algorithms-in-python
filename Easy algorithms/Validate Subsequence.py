"""
To a given two non-empty arrays of integers, determines whether the second array is a subsequence of the first one.
A subsequence of an array is a set of numbers that aren't necessarily adjacent in the array but that are in the same
order as they appear in the array.

Sample Input:                              |     Sample Output:
                                           |        True
array = [5, 1, 22, 25, 6, -1, 8, 10]       |
sequence = [1, 6, -1, 10]                  |
"""


# O(n) time | O(1) space - where n is the length of the array
def is_valid_subsequence(array, sequence):
    arr_idx = 0
    seq_idx = 0

    while arr_idx < len(array) and seq_idx < len(sequence):
        if array[arr_idx] == sequence[seq_idx]:
            seq_idx += 1
        arr_idx += 1

    return seq_idx == len(sequence)

# # O(n) time | O(1) space - where n is the length of the array
# def is_valid_subsequence(array, sequence):
#     seq_idx = 0
#
#     for value in array:
#         if seq_idx == len(sequence):
#             break
#         if sequence[seq_idx] == value:
#             seq_idx += 1
#
#     return seq_idx == len(sequence)

arr = [5, 1, 22, 25, 6, -1, 8, 10]
seq = [1, 6, -1, 10]
print(is_valid_subsequence(arr, seq))