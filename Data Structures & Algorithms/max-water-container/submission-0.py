class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        pl,pr, water = 0, n-1, 0
        while pl<pr:
            if heights[pl]<=heights[pr]:
                cw = heights[pl]*(pr-pl)
                if cw>=water:
                    water=cw
                    pl+=1
                else:
                    pl+=1
            elif heights[pl]>=heights[pr]:
                cw = heights[pr]*(pr-pl)
                if cw>=water:
                    water=cw
                    pr-=1
                else:
                    pr-=1
        return water
                