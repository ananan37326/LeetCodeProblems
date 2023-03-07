#
# @lc app=leetcode id=1004 lang=python3
#
# [1004] Max Consecutive Ones III
#

# @lc code=start
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        #declaring variables
        l = 0 # left pointer
        max_ones = 0 # number of maximum ones 
        max_length = 0 # length of the longest substring

        # looping through the array with right pointer
        for r in range(len(nums)):
            if nums[r] == 1:
                max_ones += 1

            # check if the windows size is > k +max_ones, then we update the window size
            while (r-l+1-max_ones) > k:
                if nums[l] == 1:
                    max_ones -= 1
                l += 1

            max_length = max(max_length,r-l+1)

        return max_length
        
# @lc code=end

