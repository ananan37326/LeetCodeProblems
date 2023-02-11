#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap = {i:[] for i in range(numCourses)}

        for crs, pre in prerequisites:
            premap[crs].append(pre)

        visited = set()
        def dfs(crs):
            if crs in visited:
                return False
            if premap[crs] == []:
                return True
            
            visited.add(crs)

            for pre in premap[crs]:
                if not dfs(pre):
                    return False
            
            visited.remove(crs)

            premap[crs] = []

            return True 
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True

        
# @lc code=end

