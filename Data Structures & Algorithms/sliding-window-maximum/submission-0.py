class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque()
        left=right=0 # first window: []

        while right < len(nums):
            while q and nums[q[-1]] < nums[right]: 
                # determine wheather rightest element in q less than current right bound one
                q.pop() # pop out this small one
            q.append(right) # append bigger one

            if left > q[0]: # onece left bound index > largest number index(pass it), pop that one
                q.popleft()
            
            if (right+1) >= k:
                output.append(nums[q[0]])
                left += 1
            right += 1
        return output