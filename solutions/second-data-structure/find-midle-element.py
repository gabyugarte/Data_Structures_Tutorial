
### To find the middle element in a linked list:----------------------------------------------------------


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middleNode(head):
    # Initialize two pointers slow and fast
    slow = fast = head
    
    # Traverse the list with fast moving 2 steps and slow moving 1 step
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    # Return the node pointed to by slow (middle node)
    return slow





