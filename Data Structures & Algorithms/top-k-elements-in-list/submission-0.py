class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        for i in nums:
            hm[i] = hm.get(i, 0) +1
        
        bucket = [[] for _ in range(len(nums)+1)]
        for i, n in hm.items():
             bucket[n].append(i)
        output = []
        for i in range(len(nums), 0, -1):
            for n in bucket[i]:
                output.append(n)
                if len(output) == k:
                    return output