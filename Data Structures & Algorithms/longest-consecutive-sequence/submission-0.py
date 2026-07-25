class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nset = set(nums)
        maxL = 0
        for num in nset:
            if (num-1) not in nset:
                L=1
                while (num+L) in nset:
                    L+=1
                maxL = max(L, maxL)
        return maxL
