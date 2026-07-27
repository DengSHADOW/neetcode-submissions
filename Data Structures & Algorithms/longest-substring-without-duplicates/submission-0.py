class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window=set()
        wl,r=0,0
        for wr in range(len(s)):
            while s[wr] in window:
                window.remove(s[wl])
                wl+=1
            window.add(s[wr])
            r=max(r, wr-wl+1)
        return r