# LeetCode 1047 - Remove All Adjacent Duplicates In String (Recursive)
# Base Case: string length <= 1 (no duplicates possible)
# Recursive Case: scan for first adjacent pair, remove it, recurse

class Solution:
    def removeDuplicates(self, s: str) -> str:
        # Base case: no duplicates possible
        if len(s) <= 1:
            return s
        # Find first adjacent duplicate
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                # Remove the pair and recurse
                return self.removeDuplicates(s[:i] + s[i + 2:])
        # No adjacent duplicates found
        return s
