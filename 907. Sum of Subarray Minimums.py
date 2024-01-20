class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        stack = []
        ans = 0
        
        for i, n in enumerate(arr):
            while stack and n < stack[-1][1]:
                j, m = stack.pop()
                left = j - stack[-1][0] if stack else j + 1
                right = i - j
                ans = (ans + m * left * right) % MOD
            stack.append((i, n))
            
        for i in range(len(stack)):
            j, m = stack[i]
            left = j - stack[i-1][0] if i > 0 else j + 1
            right = len(arr) - j
            ans = (ans + m * left * right) % MOD
            
        return ans