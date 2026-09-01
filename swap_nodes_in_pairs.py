# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: if list is empty or has only one node, no swap needed
        if not head or not head.next:
            return head
        
        # Store the nodes to be swapped
        first = head
        second = head.next
        
        # Recursively swap the rest of the list starting from the third node
        # The third node is head.next.next
        remaining = self.swapPairs(second.next)
        
        # Swap the first two nodes
        second.next = first
        first.next = remaining
        
        # Return the new head (which is the second node)
        return second