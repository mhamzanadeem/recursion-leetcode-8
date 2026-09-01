# LeetCode 231 - Power of Two (Recursive)
# Base Case: n == 1 (yes, it's a power of two), n <= 0 (no)
# Recursive Case: n is even -> recurse(n / 2), n is odd -> False

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # Base cases
        if n == 1:
            return True
        if n <= 0 or n % 2 != 0:
            return False
        # Recursive case: divide by 2
        return self.isPowerOfTwo(n // 2)
