class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        endbrackets = { ")" : "(", "]" : "[", "}" : "{" }
        for i in s:
            if i in endbrackets:
                if stack and stack[-1]==endbrackets[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False
