class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for i in range(len(s)):
            if stack and stack[-1][0] == s[i]:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                    stack.append([s[i], 1])
        return ''.join(i[0] * i[1] for i in stack)

#Test
s = "pbbcggttciiippooaais"
k = 2
print(Solution().removeDuplicates(s, k))
