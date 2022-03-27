"""
Program that takes in an empty array, traverses the tree using the Depth-first Search approach
(specifically navigating the tree from left to right), stores all of the nodes' names in the input array, and returns it

Sample Input:             |         Sample Output:
graph =   A               |    ['A', 'B', 'E', 'F', 'I', 'J', 'C', 'D', 'G', 'K', 'H']
        / | \             |
       B  C  D            |
     /  \   / \           |
    E    F  G  H          |
        / \  \            |
       I   J  K           |
"""


class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    # O(v + e) time | O(v) - where v is the number of verticles of the input graph
    # and e is the number of edges of the input graph
    def depthFirstSearch(self, array):
        array.append(self.name)
        for node in self.children:
            node.depthFirstSearch(array)

        return array


graph = Node("A")
graph.addChild("B").addChild("C").addChild("D")
graph.children[0].addChild("E").addChild("F")
graph.children[2].addChild("G").addChild("H")
graph.children[0].children[1].addChild("I").addChild("J")
graph.children[2].children[0].addChild("K")
print(graph.depthFirstSearch([]))