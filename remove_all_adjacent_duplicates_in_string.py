class Solution:
    def removeDuplicates(self, s: str) -> str:
        def helper(i: int, result: str) -> str:
            # Base case: processed all characters
            if i == len(s):
                return result
            
            # If result is not empty and last character matches current
            if result and s[i] == result[-1]:
                # Remove the last character (skip current duplicate)
                return helper(i + 1, result[:-1])
            else:
                # Add current character
                return helper(i + 1, result + s[i])
        
        return helper(0, "")