class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = 0
        L = []
        for v in digits:
            n = n * 10 + v
        n += 1
        while n > 0:
            L.append(n%10)
            n //= 10
        L.reverse()
        return L