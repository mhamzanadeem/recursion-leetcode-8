# LeetCode 344 - Reverse String (Recursive)
# Base Case: left >= right (pointers meet or cross)
# Recursive Case: swap s[left], s[right], then recurse with left+1, right-1

class Solution:
    def reverseString(self, s: list[str]) -> None:
        def recurse(left: int, right: int) -> None:
            # Base case: pointers have met or crossed
            if left >= right:
                return
            # Swap characters
            s[left], s[right] = s[right], s[left]
            # Recursive case: move pointers inward
            recurse(left + 1, right - 1)

        recurse(0, len(s) - 1)
