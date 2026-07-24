class Solution:

    def encode(self, strs: List[str]) -> str:
        en = ""
        for s in strs:
            en += str(len(s)) + '#' + s
        return en

    def decode(self, s: str) -> List[str]:
        de, start = [], 0
        while start < len(s):
            sepPos = start
            while s[sepPos] != '#':
                sepPos+= 1
            length = int(s[start:sepPos])
            de.append(s[sepPos+1: sepPos+1+length])
            start = sepPos +1+length
        return de