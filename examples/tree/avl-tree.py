'''AVLNode class defines the structure of a node in an AVL tree.
AVLTree class contains various methods for AVL tree operations such as getting the height of a node, 
calculating balance factor, and rotations (like rightRotate).
The rightRotate method demonstrates a single right rotation in an AVL tree to balance it.
The getHeight method returns the height of a node, and getBalance calculates the balance factor for the node.
Additional methods such as leftRotate, insert, delete, and others are required for a complete AVL tree implementation.
These methods handle balancing operations after insertions and deletions, ensuring the tree maintains its balance factor property..'''

class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def getHeight(self, node):
        if not node:
            return 0
        return node.height

    def getBalance(self, node):
        if not node:
            return 0
        return self.getHeight(node.left) - self.getHeight(node.right)

    def rightRotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y


