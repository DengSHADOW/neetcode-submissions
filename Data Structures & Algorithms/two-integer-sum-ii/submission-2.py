class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pl, pr = 0, len(numbers)-1
        while pl<pr:
            if numbers[pl]+numbers[pr]<target:
                pl+=1
            elif numbers[pl]+numbers[pr]>target:
                pr-=1
            elif numbers[pl]+numbers[pr]==target:
                return [pl + 1, pr + 1]
            