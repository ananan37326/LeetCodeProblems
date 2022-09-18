#
# @lc app=leetcode id=1041 lang=python3
#
# [1041] Robot Bounded In Circle
#

# @lc code=start
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # Directions: 0-North, 1-East, 2-South, 3-West
        direction = 0 
        movements = [(0,1),(1,0),(0,-1),(-1,0)]
        pos = (0,0)

        for ins in instructions:
            if ins == "G":
                pos = tuple(map(lambda i, j: i + j, pos, movements[direction]))
            elif ins == "L":
                direction = (direction-1)%4
            elif ins == "R":
                direction = (direction+1)%4
        
        (final_x, final_y) = pos
        if direction != 0 or (final_x==0 and final_y==0):
            return True
        else:
            return False

        
# @lc code=end

