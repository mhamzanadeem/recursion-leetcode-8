# LeetCode 206 - Reverse Linked List (Recursive + Iterative for comparison)
# Base Case: head is None or head.next is None
# Recursive Case: reverse the rest, attach head at the end

# --- Definition for singly-linked list ---
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# --- RECURSIVE SOLUTION ---
class SolutionRecursive:
    def reverseList(self, head: ListNode) -> ListNode:
        # Base case: empty list or single node
        if not head or not head.next:
            return head
        # Recursive case: reverse the rest of the list
        new_head = self.reverseList(head.next)
        # Put head at the end
        head.next.next = head
        head.next = None
        return new_head

# --- ITERATIVE SOLUTION (for comparison) ---
class SolutionIterative:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev

# --- COMPARISON ---
# Iterative: O(n) time, O(1) space - uses a loop and pointer manipulation
# Recursive: O(n) time, O(n) space - uses call stack
# Iterative is generally preferred for linked list reversal due to constant space.
# Recursive is cleaner but risks stack overflow for very long lists.
