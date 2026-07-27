class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        windo = set()
        freq = {}
        wl, r, maxc = 0,0,0
        for wr in range(len(s)):
            freq[s[wr]]=freq.get(s[wr], 0) + 1
            maxc = max(maxc, freq[s[wr]])

            while (wr-wl+1)-maxc > k:
                freq[s[wl]]-=1
                wl+=1
            r = max(r, wr-wl+1)
        return r