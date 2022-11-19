#
# @lc app=leetcode id=542 lang=python3
#
# [542] 01 Matrix
#

# @lc code=start
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        distRow = [99999] * len(mat[0])
        distMat = [distRow.copy() for i in range(len(mat))]
        
        # pass1
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    distMat[i][j] = 0
                else:
                    if i>0:
                        distMat[i][j] = min(distMat[i][j], distMat[i-1][j] + 1)
                    if j>0:
                        distMat[i][j] = min(distMat[i][j], distMat[i][j-1] + 1)


        #pass2
        for i in range(len(mat)-1,-1,-1):
            for j in range(len(mat[0])-1,-1,-1):
                if mat[i][j] == 0:
                    distMat[i][j] = 0
                else:
                    if i<len(mat)-1:
                        distMat[i][j] = min(distMat[i][j], distMat[i+1][j] + 1)
                    if j<len(mat[0])-1:
                        distMat[i][j] = min(distMat[i][j], distMat[i][j+1] + 1)
                        
        
        return distMat
		
        
# @lc code=end

