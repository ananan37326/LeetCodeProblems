class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        cache = {}

        def dfs(i):
            cur_max = 0
            res = 0

            if i in cache:
                return cache[i]

            for j in range(i, min(len(arr), i+k)):
                cur_max = max(cur_max, arr[j])
                window_size = j - i + 1
                res = max(res, dfs(j+1) + cur_max * window_size)

            cache[i] = res
            return res

        return dfs(0)
        