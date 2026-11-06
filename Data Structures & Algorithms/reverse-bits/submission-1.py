class Solution:
    def reverseBits(self, n: int) -> int:
        #num = str(format(n, 'b'))[::-1]
        #num += '0' * (32-len(num))
        num = str(format(n, '32b'))[::-1]
        num = num.replace(' ', '0')
        return int(num, 2)