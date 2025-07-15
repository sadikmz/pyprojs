class Solution:
    def trailingZeroes(self, n: int) -> int:
        trailingZero = 0
        if n < 5:
            return trailingZero
        while n >= 5:
            n //= 5
            trailingZero += n
        return trailingZero
        # Optimized solution
