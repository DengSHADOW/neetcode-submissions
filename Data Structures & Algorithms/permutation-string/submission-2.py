class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        cs1,cs2=[0]*26,[0]*26
        for i in range(len(s1)):
            cs1[ord(s1[i])-ord('a')]+=1
            cs2[ord(s2[i])-ord('a')]+=1
        
        matches = 0
        for i in range(26):
            matches+=(1 if cs1[i]==cs2[i] else 0)
        
        left=0
        for right in range(len(s1),len(s2)):
            if matches==26:
                return True
            
            cright = ord(s2[right]) - ord('a')
            cs2[cright]+=1
            if cs2[cright] == cs1[cright]:
                matches += 1
            elif cs2[cright] == cs1[cright] + 1:
                matches -= 1

            cleft = ord(s2[left]) - ord('a')
            cs2[cleft]-=1
            if cs2[cleft] == cs1[cleft]:
                matches += 1
            elif cs2[cleft] == cs1[cleft] - 1:
                matches -= 1
            left+=1
        return matches==26