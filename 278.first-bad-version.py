#
# @lc app=leetcode id=278 lang=python3
#
# [278] First Bad Version
#

# @lc code=start
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 0, n 

        while left < right:
            mid = left + (right-left)//2

            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        
        if isBadVersion(left) and left==right:
            return left
        return -1
        
# @lc code=end

