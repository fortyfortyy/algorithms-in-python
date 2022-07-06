"""
Funcion that takes in a non-empty array of distinct integers and an integer representing a target sum.
If any two numbers in the input array sum up to the target sum, the funcion should return them in an array,
in any order. The target sum has to be obtained by summing two different integers in the array can't add a single
integer to itself in order to obtain the target sum.
Assume that there will be at most one pair of numbers summing up to the target sum.

Sample Input:                                  |      Sample Output:
array_to_check = [3, 5, -4, 8, 11, 1, -1, 6]   |      [-1, 11] # the numbers could be in reverse order
target = 10                                    |
"""

# O(n) time | O(n) space - the fastest performance
def two_number_sum(array, target_sum):
    nums = {}
    for num in array:
        potential_number = target_sum - num
        if potential_number in nums:
            return [potential_number, num]
        nums[num] = True

    return []

# O(n^2) time | O(1) space - the slowest performance
# def two_number_sum(array, target_sum):
#     for idx, number in enumerate(array):
#         for idx2, number2 in enumerate(array):
#             if number + number2 == target_sum and idx != idx2:
#                 return [number, number2]
#     return []

# # O(nlog(n)) | O(1) space - the average performance
# def two_number_sum(array, target_sum):
#     array.sort()
#     left = 0
#     right = len(array) - 1
#     while left < right:
#         sum_arr = array[left] + array[right]
#         if sum_arr == target_sum:
#             return [array[right], array[left]]
#         elif sum_arr > target_sum:
#             right -= 1
#         else:
#             left += 1
#     return []


array_to_check = [3, 5, -4, 8, 11, 1, -1, 6]
target = 10
print(two_number_sum(array_to_check, target))