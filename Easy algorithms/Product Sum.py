"""
Function that takes in a "special" array and returns its product sum.
A "special" array is a non-empty array that contains either integers or other "special" arrays.
The product sum of a "special" array is the sum of its elements, where "special" arrays inside it are summed themselves
and then multipled by their level of depth.

A depth of a "special" array is how far nested it is. For instance, the depth of [] is 1; the depth of the inner array
[[]] is 2; the depth of the innermost array [[[]]] is 3.

Therefore, the product sum of [x, y] is x + y; the product sum of [x, [y, z]] is x + 2 * (y + z);
the product sum of [x, [y , [z]]] is x + 2 * (y + 3z).

Sample input:                                   |           Sample Output:
array = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]    |            12     # calculated as: 5 + 2 + 2 * (7 - 1) + 3 + 2 * (6 + 3 * (-13 + 8) + 4)
"""

# O(n) time | O(d) space - where n is the number of elements in the array,
# including sub-elements, and d is the greatest depth of "sepcial" arrays in the array
def product_sum(array, multiplier=1):
    result = 0
    for element in array:
        if isinstance(element, list):
            result += product_sum(element, multiplier + 1)
        else:
            result += element

    return result * multiplier


array = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
print(product_sum(array))