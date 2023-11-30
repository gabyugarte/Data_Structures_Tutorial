### To reverse a linked list:--------------------------------------------------------------------------------

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    # Initialize pointers: prev (previous), current, next_node
    prev = None
    current = head
    
    # Iterate through the list to reverse the links
    while current:
        next_node = current.next      # Store the next node
        current.next = prev           # Reverse the link
        prev = current                # Move prev to current
        current = next_node           # Move current to next node
    
    # Return the new head of the reversed linked list
    return prev