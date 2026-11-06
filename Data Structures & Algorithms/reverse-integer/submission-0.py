class Solution:
    def reverse(self, x: int) -> int:
        s = int(str(abs(x))[::-1])
        if x < 0:
            s = -s
        return s if s > -2**31 and s< 2**31 - 1 else 0