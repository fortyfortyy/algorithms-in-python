"""
Function that takes in a Binary Search Tree (BST) and a target integer value and returns the closest value to that
target value contained in the BST.

Assume that there will only be one closest value.

Each BST node has an integer value, a left child node, and a right child node. A node is said to be a valid BST node
if and only if it satisfies the BST property: its value is strictly greater than the values of every node to its left;
its value is less than or equal to the values of every node to its right; and its children nodes are either valid BST
nodes themselves or None / null.

Sample Input:                  |         Sample Output:
tree =   10                    |              13
       /    \                  |
      5      15                |
     /      /  \               |
    2      13   22             |
   /         \                 |
  1          14                |
                               |
target = 12                    |
"""


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def find_closest_value_in_bst(tree, target):
    return find_closest_value_in_bst_helper(tree, target, tree.value)


# First Solution (recursive algorithm)
# Average:  O(log(n)) time | O(log(n)) space
# Worst:    0(n) time | O(n) space
def find_closest_value_in_bst_helper(node, target, closest):
    if node is None:
        return closest

    if abs(target - closest) > abs(target - node.value):
        closest = node.value

    if target > node.value:
        return find_closest_value_in_bst_helper(node.right, target, closest)
    elif target < node.value:
        return find_closest_value_in_bst_helper(node.left, target, closest)
    return closest


# # Second Solution (iterative algorithm)
# # Average:  O(log(n)) time | O(1) space
# # Worst:    0(n) time | O(1) space
# def find_closest_value_in_bst_helper(tree, target, closest):
#     current_node = tree
#
#     while current_node is not None:
#         if abs(target - closest) > abs(target - current_node.value):
#             closest = current_node.value
#
#         if target > current_node.value:
#             current_node = current_node.right
#         elif target < current_node.value:
#             current_node = current_node.left
#         else:
#             break
#
#     return closest


tree = BST(10)
tree.left = BST(5)
tree.left.left = BST(2)
tree.left.left.left = BST(1)
tree.left.right = BST(5)
tree.right = BST(15)
tree.right.left = BST(13)
tree.right.left.right = BST(14)
tree.right.right = BST(22)

print(find_closest_value_in_bst(tree, target=12))
