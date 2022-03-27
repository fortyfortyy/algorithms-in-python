"""
Function that takes in a non-empty array of distinct integers and an integer representing a target sum. The function
find all triplets in the array that sum up to the target sum and return a two-dimensional array of all these triplets.
The number in each triplet is ordered in ascending order and the triplets themselves are ordered in ascending order
with respect to the number they hold.

If no three numbers sup up to the target sum. the function returns an empty array.

        Sample Input                            |               Sample Output
array = [12, 3, 1, 2, -6, 5, -8, 6]             |   [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]
target_sum = 0
"""

# O(n^2)) time | O(n) space - where n is the length of the input array
def three_number_sum(array, target):
    array.sort()

    triples = []
    for i in range(len(array) - 2):
        left = i + 1
        right = len(array) - 1

        while left < right:
            current_sum = array[i] + array[left] + array[right]
            if current_sum == target:
                triples.append(sorted([array[i], array[left], array[right]]))
                left += 1
                right -= 1
            elif current_sum < target:
                left += 1
            else:
                right -= 1

    return triples


array = [12, 3, 1, 2, -6, 5, -8, 6]
target = 0
print(three_number_sum(array, target))