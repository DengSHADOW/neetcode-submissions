class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        optrs = {'+', '-', '*', '/'}
        stack = []

        for i in tokens:
            if stack and i in optrs:
                int2 = stack.pop()
                int1 = stack.pop()
                if i == '+':
                    stack.append(int1 + int2)
                elif i == '-':
                    stack.append(int1 - int2)
                elif i == '*':
                    stack.append(int1 * int2)
                elif i == '/':
                    stack.append(int(int1 / int2))
            else: stack.append(int(i))
        return stack[-1]