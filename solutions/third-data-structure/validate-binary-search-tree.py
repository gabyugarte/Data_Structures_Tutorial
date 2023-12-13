class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isValidBST(root):
    def validate(node, lower=float('-inf'), upper=float('inf')):
        if not node:
            return True

        if node.val <= lower or node.val >= upper:
            return False

        return (validate(node.left, lower, node.val) and
                validate(node.right, node.val, upper))

    return validate(root)

'''Step-by-Step Explanation:

TreeNode class: Defines a simple structure for the tree nodes, each containing a value (val), a left child (left), and a right child (right).

isValidBST function:

Defines a nested function validate that takes the current node, along with lower and upper bounds initialized as negative and positive infinity, respectively.
Validation Function (validate):

Checks if the current node is None. If so, returns True.
Validates if the current node's value violates the BST property (i.e., if it's not within the lower and upper bounds). If violated, returns False.
Recursively calls the validate function for the left child, updating the upper bound to the current node's value and keeping the lower bound unchanged.
Recursively calls the validate function for the right child, updating the lower bound to the current node's value and keeping the upper bound unchanged.
Returns the result of the logical AND operation between the validations of the left and right subtrees.
Returns the Result: Calls the validate function with the root of the tree and returns the result, determining if the given binary tree is a valid BST or not.'''
