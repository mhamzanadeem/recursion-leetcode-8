# LeetCode 125 - Valid Palindrome (Recursive)
# Base Case: left >= right (all characters checked)
# Recursive Case: compare s[left] and s[right], recurse with left+1, right-1

class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ''.join(c.lower() for c in s if c.isalnum())

        def recurse(left: int, right: int) -> bool:
            # Base case: pointers met or crossed
            if left >= right:
                return True
            # Characters don't match
            if cleaned[left] != cleaned[right]:
                return False
            # Recursive case: check inner substring
            return recurse(left + 1, right - 1)

        return recurse(0, len(cleaned) - 1)
