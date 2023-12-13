'''The RBNode class represents a node in the Red-Black Tree. It contains attributes such as key (the node's value), left, right 
(pointers to left and right child nodes), parent (pointer to the parent node), and color (either "Red" or "Black").
*The RedBlackTree class initializes an empty tree with a root node set to None.
*The left_rotate and right_rotate methods are used for performing left and right rotations, respectively, 
to maintain the Red-Black Tree properties during insertions.
*The insert method adds a new node with a given key into the Red-Black Tree.
It starts by creating a new node with the provided key and then traverses the tree to find the appropriate position for insertion similar to a standard binary search tree.
Once the node is placed in its correct position, it calls the fix_violations method to ensure that the Red-Black Tree properties are maintained.
'''


class RBNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.color = "Red"  # By default, new nodes are red

class RedBlackTree:
    def __init__(self):
        self.root = None

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left:
            y.left.parent = x
        y.parent = x.parent
        if not x.parent:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right:
            x.right.parent = y
        x.parent = y.parent
        if not y.parent:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
        x.right = y
        y.parent = x

    def insert(self, key):
        node = RBNode(key)
        y = None
        x = self.root
        while x:
            y = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if not y:
            self.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node

        self.fix_violations(node)

    def fix_violations(self, node):
        while node != self.root and node.parent.color == "Red":
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle and uncle.color == "Red":
                    node.parent.color = "Black"
                    uncle.color = "Black"
                    node.parent.parent.color = "Red"
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.color = "Black"
                    node.parent.parent.color = "Red"
                    self.right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle and uncle.color == "Red":
                    node.parent.color = "Black"
                    uncle.color = "Black"
                    node.parent.parent.color = "Red"
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = "Black"
                    node.parent.parent.color = "Red"
                    self.left_rotate(node.parent.parent)

        self.root.color = "Black"  # Ensure root node is black

# Usage example:
rb_tree = RedBlackTree()
keys = [7, 3, 18, 10, 22, 8, 11, 26]
for key in keys:
    rb_tree.insert(key)

