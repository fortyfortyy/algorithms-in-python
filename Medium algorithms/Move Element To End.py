"""
Function that takes in an array of integers and an integer, moves all instances of that integer in the array to the end
of the array and returns the array.

Funcion perform this in place (mutate the input array) and doesn't need to maintain the order of the other integers.

       Sample Input                     |       Sample Output
array = [2, 1, 2, 2, 2, 3, 4, 2]        |    [1, 3, 4, 2, 2, 2, 2, 2]
to_move = 2
"""
# O(n) time | O(1) space - where n is the length of the array

def move_element_to_end(array, toMove):
    left = 0
    right = len(array) - 1

    while left < right:
        if array[left] == toMove and array[right] != toMove:
            array[left], array[right] = array[right], array[left]
        elif array[right] == toMove:
            right -= 1
            continue

        left += 1

    return array


print(move_element_to_end(array=[2, 1, 2, 2, 2, 3, 4, 2], toMove=2))
