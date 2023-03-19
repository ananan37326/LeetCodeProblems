#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)

        if total_sum % 2 != 0:
            return False
        
        target = total_sum // 2

        dp =  [False] * (target+1)
        dp[0] = True 

        for num in nums:
            for s in range(target, num-1, -1):
                dp[s] = dp[s] | dp[s-num]
        
        return dp[target]

        
# @lc code=end

