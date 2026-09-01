class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Helper recursive function
        def helper(left: int, right: int, chars: str) -> bool:
            # Base case: if pointers cross, it's a palindrome
            if left >= right:
                return True
            
            # Skip non-alphanumeric characters from left
            if not chars[left].isalnum():
                return helper(left + 1, right, chars)
            
            # Skip non-alphanumeric characters from right
            if not chars[right].isalnum():
                return helper(left, right - 1, chars)
            
            # Compare characters (case insensitive)
            if chars[left].lower() != chars[right].lower():
                return False
            
            # Move both pointers inward
            return helper(left + 1, right - 1, chars)
        
        # Start recursion with the whole string
        return helper(0, len(s) - 1, s)