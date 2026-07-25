class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        pre=[0]*n
        suf=[0]*n
        pre[0]=height[0]
        suf[n-1]=height[n-1]
        water=0
        for i in range(1,n):
            pre[i]=max(pre[i-1],height[i])
        for i in range(n-2,-1,-1):
            suf[i]=max(suf[i+1],height[i])
        for i in range(n):
            water+=min(pre[i],suf[i])-height[i]
        return water
                
      