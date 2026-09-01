# LeetCode 24 - Swap Nodes in Pairs (Recursive)
# Base Case: head is None or head.next is None (0 or 1 node left)
# Recursive Case: swap current pair, then recurse on the rest

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # Base case: 0 or 1 node
        if not head or not head.next:
            return head
        # Save the second node (will become new head of this pair)
        second = head.next
        # Recurse on the rest after the pair
        head.next = self.swapPairs(second.next)
        # Point second node back to first
        second.next = head
        # Return second as new head of this pair
        return second
