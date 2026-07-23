from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = defaultdict(list)
        for word in strs:
            alst = [0]*26
            for i in word:
                alst[ord(i)-ord('a')] += 1
            output[tuple(alst)].append(word)
        return list(output.values())