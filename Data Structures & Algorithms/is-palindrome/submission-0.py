class Solution:
    def isPalindrome(self, s: str) -> bool:
        pl, pr = 0, len(s)-1
        while pl<pr:
            while pl<pr and not s[pl].isalnum():
                pl+=1
            while pl<pr and not s[pr].isalnum():
                pr-=1
            if s[pr].lower()!=s[pl].lower():
                return False
            pl+=1
            pr-=1
        return True