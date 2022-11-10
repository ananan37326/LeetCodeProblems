#
# @lc app=leetcode id=733 lang=python3
#
# [733] Flood Fill
#

# @lc code=start
class Solution:
    def fill(self,image,sr,sc,color,newColor):
        if (sr<0 or sc<0 or sr>=len(image) or sc>=len(image[0]) or image[sr][sc]!=color):
            return
        image[sr][sc] = newColor
        
        self.fill(image,sr-1,sc,color,newColor)
        self.fill(image,sr+1,sc,color,newColor)
        self.fill(image,sr,sc-1,color,newColor)
        self.fill(image,sr,sc+1,color,newColor)
    
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if (image[sr][sc]==color):
            return image
        self.fill(image,sr,sc,image[sr][sc],color)
        return image
        
        
# @lc code=end

