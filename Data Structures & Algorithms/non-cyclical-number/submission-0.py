class Solution:
    def isHappy(self, n: int) -> bool:
        seen = {n}
        while n != 1:
            n = self.happy(n)
            if n in seen:
                return False
            seen.add(n)
        return True
        
    def happy(self, n: int) -> int:
        res = 0
        while n > 0:
            res += (n % 10) ** 2
            n //= 10
        return res