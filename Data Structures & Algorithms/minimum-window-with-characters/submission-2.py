class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return False # False for none
        
        ct,window = {}, {}
        # count of each char in string t. Slide window chars
        
        for c in t: ct[c] = 1 + ct.get(c,0)
        # Loop t to update ct

        types = len(ct)
        # Number of types(of character) in ct need to fullfil
        fullfil = 0
        # Number of matched char in slide window
        windowA, windowL = [-1, -1], float("infinity")
        # window area and length of window
        left = 0 # left bound of window
        for right in range(len(s)): 
            ch = s[right] # Loop s and set current as right bound of window
            window[ch] = 1 + window.get(ch, 0) # Update window in each loop
            if ch in ct and window[ch] == ct[ch]:
                fullfil += 1 # Inc fullfil as match for window and ct
            
            while fullfil == types: # Check fullfil
                if (right -left + 1) < windowL: # if shorter substring
                    windowA = [left, right]
                    windowL = (right -left + 1) # update
                window[s[left]] -= 1 # move left bound to right with 1
                if s[left] in ct and window[s[left]] < ct[s[left]]: # check the removed one fullfil in t
                    fullfil -= 1
                left += 1 # left ++
            
        left, right = windowA # update bound
        
        return s[left: right+1] if windowL != float("infinity") else ""

