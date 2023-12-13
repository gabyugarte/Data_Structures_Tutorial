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

'''Walkthrough of the reverseList function
Initialization of Pointers: prev is set to None, and current initially points to the head of the linked list.
Reversing the Links:
Within the while loop, next_node temporarily stores the next node to prevent losing the reference while manipulating the pointers.
current.next is set to prev, effectively reversing the link between the current node and the previous node.
prev is updated to current to progress to the next node during the next iteration.
current is updated to next_node to move to the original next node.
The loop continues until current becomes None, indicating the end of the original list. Finally, the function returns prev, which is now the new head of the reversed linked list.'''