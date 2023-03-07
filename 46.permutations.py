#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        if len(nums) == 1:
            return [nums[:]]

        for i in range(len(nums)):
            n = nums.pop(0)

            perms = self.permute(nums)

            for perm in perms:
                perm.append(n)

            result.extend(perms)
            nums.append(n)

        return result
        
# @lc code=end

