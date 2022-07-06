"""
Function that takes in two non-empty arrays of integers, finds the pair of numbers (one from each array) whose
absolute difference is closest to zero, and returns an array containing these two numbers, with the number from
the first array in the first position.

The absolute difference of two integers is the distance between them on the real number line. For example,
the absolute difference of -5 and 5 is 10, and the absolute difference of -5 and -4 is 1.
Assume that there will be one pair of numbers with the smallest difference.

        Sample Input                            |               Sample Output
array_one = [-1, 5, 10, 20, 28, 3]              |                 [28,26]
array_two = [26, 134, 135, 15, 17]
"""

# O(nlog(n) + mlog(m)) time | O(1) space - where n is the lenght of the first input array
# and m is the lenght of the second input array
def smallest_difference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()

    smallest = float('inf')
    smallestResult = []

    idxOne = 0
    idxTwo = 0

    while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):
        firstNum = arrayOne[idxOne]
        secondNum = arrayTwo[idxTwo]

        if firstNum < secondNum:
            current = secondNum - firstNum
            idxOne += 1
        elif firstNum > secondNum:
            current = firstNum - secondNum
            idxTwo += 1
        else:
            return [firstNum, secondNum]

        if smallest > current:
            smallest = current
            smallestResult = [firstNum, secondNum]

    return smallestResult


array_one = [-1, 5, 10, 20, 28, 3]
array_two = [26, 134, 135, 15, 17]

print(smallest_difference(array_one, array_two))