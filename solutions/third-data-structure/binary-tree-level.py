
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root):
    if not root:
        return []

    result = []
    queue = [root]

    while queue:
        level = []
        size = len(queue)

        for _ in range(size):
            node = queue.pop(0)
            level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level)

    return result

'''Step-by-Step Explanation:

TreeNode class: Defines a simple structure for the tree nodes, each containing a value (val), a left child (left), and a right child (right).

levelOrder function:

Checks if the root of the tree is empty. If so, returns an empty list.
Initializes an empty list result to store the level order traversal.
Initializes a queue queue with the root node.
Level Order Traversal using BFS:

While the queue is not empty:
Initializes an empty list level to store nodes at the current level.
Retrieves the current size of the queue (size).
Iterates through the elements in the queue up to size:
Removes the first node from the queue (node = queue.pop(0)).
Appends the value of the node to the level list.
Adds any existing left and right children of the current node to the queue if they exist.
Appends the level list (representing nodes at the current level) to the result.
Returns the Result: Returns the result, containing the level order traversal of the binary tree.'''