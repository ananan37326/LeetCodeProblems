#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        toBeMatched = nums[0]
        idx = 1
        for i in range(1,len(nums)):
            if nums[i] != toBeMatched:
                nums[idx] = nums[i]
                toBeMatched = nums[i]
                idx += 1
        return idx
        
# @lc code=end

