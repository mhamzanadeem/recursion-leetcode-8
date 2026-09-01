# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Edge case: if list has only one node, return None
        if head is None or head.next is None:
            return None
        
        # Recursive helper that returns the node to delete
        def delete_middle_helper(slow: ListNode, fast: ListNode, prev: ListNode = None) -> ListNode:
            # Base case: fast reached the end
            if fast is None or fast.next is None:
                # Delete the middle node (slow)
                prev.next = slow.next
                return head
            
            # Recursive case: move slow one step and fast two steps
            return delete_middle_helper(slow.next, fast.next.next, slow)
        
        return delete_middle_helper(head, head)