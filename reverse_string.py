class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def helper(left: int, right: int) -> None:
            # Base case: if left pointer crosses right pointer, stop
            if left >= right:
                return
            
            # Swap characters at left and right
            s[left], s[right] = s[right], s[left]
            
            # Recursively reverse the inner substring
            helper(left + 1, right - 1)
        
        # Start the recursion
        helper(0, len(s) - 1)