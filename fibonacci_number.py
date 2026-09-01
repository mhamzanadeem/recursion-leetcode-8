# LeetCode 509 - Fibonacci Number (Recursive)
# Base Case: f(0) = 0, f(1) = 1
# Recursive Case: f(n) = f(n-1) + f(n-2)

class Solution:
    def fib(self, n: int) -> int:
        # Base cases
        if n == 0:
            return 0
        if n == 1:
            return 1
        # Recursive case
        return self.fib(n - 1) + self.fib(n - 2)
