#
# @lc app=leetcode id=643 lang=python3
#
# [643] Maximum Average Subarray I
#

# @lc code=start
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        prevSum = 0
        for i in range(k):
            prevSum += nums[i]
        maxSum = prevSum
        for i in range(k,len(nums)):
            prevSum = prevSum + nums[i] - nums[i-k]
            if prevSum > maxSum:
                maxSum = prevSum
        return maxSum/k
        
# @lc code=end

