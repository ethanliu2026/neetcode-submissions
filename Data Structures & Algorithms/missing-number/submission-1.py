class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = set(nums)
        s = set(range(max(nums)+1))
        L = list(s - n)
        return L[0] if len(L) == 1 else max(nums) + 1