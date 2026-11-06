class Solution:
    def reverseBits(self, n: int) -> int:
        num = str(format(n, 'b'))[::-1]
        num += '0' * (32-len(num))
        return int(num, 2)