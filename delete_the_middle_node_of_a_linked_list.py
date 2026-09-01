# LeetCode 2095 - Delete the Middle Node of a Linked List (Recursive)
# Base Case: head is None or head.next is None (0 or 1 node)
# Recursive Case: use a counter to find the middle, delete it

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head: ListNode) -> ListNode:
        # Base case: 0 or 1 node
        if not head or not head.next:
            return None

        # Count total nodes
        def count_nodes(node: ListNode) -> int:
            if not node:
                return 0
            return 1 + count_nodes(node.next)

        total = count_nodes(head)
        middle = total // 2

        # Recursively find and delete middle node
        def recurse(node: ListNode, index: int) -> ListNode:
            if index == middle - 1:
                # Skip the middle node
                node.next = node.next.next
                return node
            node.next = recurse(node.next, index + 1)
            return node

        return recurse(head, 0)
