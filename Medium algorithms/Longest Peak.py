"""
Function that takes in an array of integers and returns the length of the longest peak in the array.
A peak is defined as adjacent integers in the array that are strictly increasing until they reach a tip
(the highest value in the peak), at which point they become strictly decreasing. At least three integers are required
to form a peak.

        Sample Input                                    |               Sample Output
array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]      |   6 // 0, 10, 6, 5, -1, -3
"""


# O(n) time | O(1) space - where n is the length of the input array
def longest_peak(array: [int]) -> int:
    longest_peak_length = 0
    i = 1

    while i < len(array) - 1:
        is_peak = array[i] > array[i - 1] and array[i] > array[i + 1]
        if not is_peak:
            i += 1
            continue

        left_idx = i - 2
        while left_idx >= 0 and array[left_idx] < array[left_idx + 1]:
            left_idx -= 1

        right_idx = i + 2
        while right_idx < len(array) and array[right_idx] < array[right_idx - 1]:
            right_idx += 1

        current_peak_length = right_idx - left_idx - 1
        longest_peak_length = max(longest_peak_length, current_peak_length)
        i = right_idx

    return longest_peak_length


a = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
print(longest_peak(a))