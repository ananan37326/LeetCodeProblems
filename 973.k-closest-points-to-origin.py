#
# @lc app=leetcode id=973 lang=python3
#
# [973] K Closest Points to Origin
#

# @lc code=start
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def euclidean(x,y):
            return x*x + y*y 
        
        heap = []
        
        for i in range(len(points)):
            elem = (-1 * euclidean(points[i][0],points[i][1]),i)
            
            if len(heap) == k:
                heapq.heappushpop(heap,elem)
            else:
                heapq.heappush(heap,elem)
        
        
        return [points[i] for (_,i) in heap]
        
# @lc code=end

