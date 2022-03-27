"""
Function that takes in a Binary Tree and returns a list of its branch sums ordered from leftmost branch sum to
rightmost branch sum. A branch sum is the sum of all values in a Binary Tree branch.

A Binary Tree branch is a path of nodes in a tree that starts at the root node and ends at any leaf node.

Sample Input:                  |         Sample Output:
tree =    1                    |          [15, 16, 18, 10, 11]
       /    \                  |          # 15 == 1 + 2 + 4 + 8
      2      3                 |          # 16 == 1 + 2 + 4 + 9
     / \    /  \               |          # 18 == 1 + 2 + 5 + 10
    4   5  6    7              |          # 10 == 1 + 3 + 6
   / \   \                     |          # 11 == 1 + 3 + 7
  8   9  10                    |

"""


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# recursive algorithm
# O(n) time | O(n) space - where n is the number of nodes in the Binary Tree
def branch_sum(root):
    sums = []
    branch_sum_helper(root, sums)
    return sums


def branch_sum_helper(node, sums, running_sum=0):
    if node is None:
        return

    running_sum += node.value
    if node.left is None and node.right is None:
        return sums.append(running_sum)

    branch_sum_helper(node.left, sums, running_sum)
    branch_sum_helper(node.right, sums, running_sum)


tree = BinaryTree(1)
tree.left = BinaryTree(2)
tree.left.left = BinaryTree(4)
tree.left.left.left = BinaryTree(8)
tree.left.left.right = BinaryTree(9)
tree.left.right = BinaryTree(5)
tree.left.right.left = BinaryTree(10)
tree.right = BinaryTree(3)
tree.right.left = BinaryTree(6)
tree.right.right = BinaryTree(7)

print(branch_sum(tree))
