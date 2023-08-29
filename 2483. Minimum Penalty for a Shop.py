class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        pre = [0] * (n+1)
        post = [0] * (n+1)

        for i in range(1,n+1):
            pre[i] = pre[i-1]
            if customers[i-1] == "N":
                pre[i] += 1
        
        for i in range(n - 1, -1, -1):
            post[i] = post[i+1]
            if customers[i] == "Y":
                post[i] += 1

        ans, idx = float("inf"), 0
        for i in range(n+1):
            if pre[i] + post[i] < ans:
                ans = pre[i] + post[i]
                idx = i

        return idx

s = Solution()
print(s.bestClosingTime("YYNY"))