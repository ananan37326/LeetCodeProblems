#
# @lc app=leetcode id=228 lang=python3
#
# [228] Summary Ranges
#

# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []

        final_list = []
        start = nums[0]
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1] + 1:
                end = nums[i-1]
                if start == end:
                    final_list.append(f'{start}')
                else:
                    final_list.append(f'{start}->{end}')
                start = nums[i]
        end = nums[-1]
        if start == end:
            final_list.append(f'{start}')
        else:
            final_list.append(f'{start}->{end}')
        
        return final_list

        
# @lc code=end

