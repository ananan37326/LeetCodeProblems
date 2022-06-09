class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = []
        for i in s:
            if i == '(' or i == '[' or i == '{':
                parentheses.append(i)
            else:
                if len(parentheses) == 0:
                    return False
                if i == ')' and parentheses[-1] == '(':
                    parentheses.pop()
                elif i == ']' and parentheses[-1] == '[':
                    parentheses.pop()
                elif i == '}' and parentheses[-1] == '{':
                    parentheses.pop()
                else:
                    return False
        if len(parentheses) == 0:
            return True
        else:
            return False


# Test
s = "([)]{"
print(Solution().isValid(s))

