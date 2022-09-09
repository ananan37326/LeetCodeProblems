#
# @lc app=leetcode id=566 lang=python3
#
# [566] Reshape the Matrix
#

# @lc code=start
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r*c != len(mat) * len(mat[0]):
            return mat
        final_mat = []
        temp_list = []
        cc = 0

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                temp_list.append(mat[i][j])
                #print(temp_list)
                cc += 1
                if cc == c:
                    final_mat.append(temp_list.copy())
                    temp_list = []
                    cc = 0
                
                    
        
        return final_mat

        
# @lc code=end

