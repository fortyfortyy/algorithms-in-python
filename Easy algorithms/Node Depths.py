"""
Function that takes in a Binary Tree and returns the sum of its nodes' depths.

Sample Input:                 |         Sample Output:
tree =   1                    |          16
       /   \                  |          # The depth of the node with value 2 is 1
      2     3                 |          # The depth of the node with value 3 is 1
     / \   /  \               |          # The depth of the node with value 4 is 2
    4   5 6    7              |          # The depth of the node with value 5 is 2
   / \                        |          # Etc ...
  8   9                       |          # Summing all of these depths yields 16
"""


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# First Solution (recursive algorithm)
# O(n) time | O(h) space - where n is the number of the nodes in the Binary Tree and h is the height of the Binary Tree
def node_depths(root, sums=0):
    if root is None:
        return 0

    return sums + node_depths(root.left, sums + 1) + node_depths(root.right, sums + 1)

# # Second Solution (iterative algorithm)
# # O(n) time | O(h) space - where n is the number of the nodes in the Binary Tree and h is the height of the Binary Tree
# def node_depths(root):
#     sum_of_depths = 0
#     stack = [{'node': root, 'depth': 0}]
#
#     while len(stack) > 0:
#         node_info = stack.pop()
#         node, depth = node_info['node'], node_info['depth']
#
#         if node is None:
#             continue
#
#         sum_of_depths += depth
#         if node.left is not None:
#             stack.append({'node': node.left, 'depth': depth + 1})
#         if node.right is not None:
#             stack.append({'node': node.right, 'depth': depth + 1})
#
#     return sum_of_depths


tree = BinaryTree(1)
tree.left = BinaryTree(2)
tree.left.right = BinaryTree(5)
tree.left.left = BinaryTree(4)
tree.left.left.left = BinaryTree(8)
tree.left.left.right = BinaryTree(9)
tree.right = BinaryTree(3)
tree.right.left = BinaryTree(6)
tree.right.right = BinaryTree(7)

print(node_depths(tree))
