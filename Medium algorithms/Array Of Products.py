"""
Function that takes in a non-empty array of integers and returns an array of the same length, where each element
in the output array is equal to the product of every other number in the input array.

In other words, the value at output[i] is equal to the product of every number in the input array other than input[i].
Note that you're expected to solve this problem without using division.

        Sample Input          |         Sample Output
array = [5, 1, 4, 2]          |     [8, 40, 10, 20]
                                    // 8  is equal to 1 x 4 x 2
                                    // 40 is equal to 5 x 4 x 2
                                    // 10 is equal to 5 x 1 x 2
                                    // 20 is equal to 5 x 1 x 4
"""
# O(n) time | O(n) space - where n is the length of the input array
def array_of_products(array: []) -> []:
    current_product_idx = 0
    products = []

    while current_product_idx < len(array):

        temporary_result = 1
        left_idx = current_product_idx - 1
        while left_idx >= 0:
            temporary_result *= array[left_idx]
            left_idx -= 1

        right_idx = current_product_idx + 1
        while right_idx < len(array):
            temporary_result *= array[right_idx]
            right_idx += 1

        current_product_idx += 1
        products.append(temporary_result)

    return products


print(array_of_products(array=[5, 1, 4, 2]))