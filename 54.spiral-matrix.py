#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0]) 
        total_cells = rows*cols
        visited = set()
        dir = 0
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]

        res = []

        def traverse(r,c, dir):
            dirY,dirX = dirs[dir][0], dirs[dir][1]
            
            if len(visited) == total_cells:
                return res
            
            
            print((r+dirY,c+dirX))
            if ((r+dirY,c+dirX) in visited) or (r+dirY)>=rows or (r+dirY)<0 or (c+dirX)>=cols or (c+dirX)<0:
                #change direction
                dir = (dir+1) % 4
                dirY,dirX = dirs[dir][0], dirs[dir][1]

            
            res.append(matrix[r][c])
            visited.add((r,c))
            print(res)

            traverse(r+dirY, c+dirX, dir)

        traverse(0, 0, dir)

        return res 

        

s = Solution()
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
s.spiralOrder(matrix)           
            

        
# @lc code=end

