#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#

# @lc code=start
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        q = collections.deque()
        fresh_oranges = 0
        time = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh_oranges += 1
                elif grid[r][c] == 2:
                    q.append((r,c))

        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        while q and fresh_oranges >0:

            for i in range(len(q)):

                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = r+dr, c+dc
                    if (row<0 or row>=ROWS
                        or col<0 or col>=COLS
                        or grid[row][col]!=1):
                        continue

                    grid[row][col] = 2

                    fresh_oranges -= 1
                    q.append((row,col))
            time +=1

        return time if fresh_oranges == 0 else -1 

        
# @lc code=end

