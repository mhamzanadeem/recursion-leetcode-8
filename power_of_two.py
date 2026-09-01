class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # Base cases
        if n <= 0:
            return False
        if n == 1:
            return True
        # If n is odd and > 1, it's not a power of two
        if n % 2 != 0:
            return False
        # Recursively divide by 2
        return self.isPowerOfTwo(n // 2)