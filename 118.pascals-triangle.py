#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1],[1,1]]
        else:
            final_list = [[1],[1,1]]
            for i in range(3,numRows+1):
                temp = []
                temp.append(1)
                for j in range(1,i-1):
                    temp.append(final_list[-1][j-1] + final_list[-1][j])
                temp.append(1)
                final_list.append(temp.copy())
            return final_list
# @lc code=end

