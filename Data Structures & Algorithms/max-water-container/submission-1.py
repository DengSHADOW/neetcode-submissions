class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        pl,pr, water = 0, n-1, 0
        while pl<pr:
            h = min(heights[pr],heights[pl])
            w = pr-pl
            water = max(h*w, water)
            if heights[pr] > heights[pl]:
                pl+=1
            else:
                pr-=1
        return water
                