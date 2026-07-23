class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        appear = []
        for i in nums:
            if i in appear:
                return True
            else:
                appear.append(i)
        return False