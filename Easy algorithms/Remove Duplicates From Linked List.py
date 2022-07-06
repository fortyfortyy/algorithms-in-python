"""
You're given the head of a Singly Linked List whose nodes are in sorted order with respect to their values.
Function has to return a modified version of the Linked List that doesn't contain any nodes with duplicate values.
The Linked List should be modified in place and the modified Linked List should still have its nodes sorted with
respect to their values.

Sample input:                                               |       Sample Output:
linked_list = 1 -> 1 -> 3 -> 4 -> 4 -> 4 -> 5 -> 6 -> 6     |     1 -> 3 -> 4 -> 5 -> 6  # the head node with value 1
"""

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# O(n) time | O(1) space - where n is the number of nodes in the Linked List
def remove_duplicates_from_linked_list(linked_list):
    current_node = linked_list

    while current_node is not None:
        next_node = current_node.next
        while next_node is not None and current_node.value == next_node.value:
            next_node = next_node.next

        current_node.next = next_node
        current_node = next_node

    return linked_list