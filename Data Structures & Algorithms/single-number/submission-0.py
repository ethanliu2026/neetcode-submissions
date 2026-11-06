class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = set()
        s = set()
        for n in nums:
            if n not in seen:
                seen.add(n)
            else:
                s.add(n)
        d = seen - s
        return list(d)[0]