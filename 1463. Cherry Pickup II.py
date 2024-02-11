class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        cache = {}
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c1, c2):
            if (r, c1, c2) in cache:
                return cache[(r, c1, c2)]
            
            if c1 == c2 or min(c1, c2) < 0 or max(c1, c2) >= COLS:
                return 0

            if r == ROWS - 1:
                return grid[r][c1] + grid[r][c2]

            res = 0
            pos = [-1, 0, 1]

            for c1_d in pos:
                for c2_d in pos:
                    res = max(res, dfs(r+1, c1 + c1_d, c2 + c2_d))

            cache[(r, c1, c2)] = res + grid[r][c1] + grid[r][c2]

            return cache[(r, c1, c2)]

        return dfs(0, 0, COLS-1)
        