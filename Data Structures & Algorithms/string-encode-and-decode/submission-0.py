class Solution:

    def encode(self, strs: List[str]) -> str:
        en = ""
        for s in strs:
            en += str(len(s)) + '#' + s
        return en

    def decode(self, s: str) -> List[str]:
        de = []
        start = 0
        while start < len(s):
            sepPos = start
            while s[sepPos] != '#':
                sepPos+= 1
            length = int(s[start:sepPos])
            start = sepPos +1
            de.append(s[start: start+length])
            start+=length
        return de