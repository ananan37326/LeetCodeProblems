#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#

# @lc code=start
class Solution:

    def reversenums(self,nums,left,right):
        l,r = left, right

        while l<r:
            nums[l], nums[r] = nums[r], nums[l]
            l,r = l+1, r-1

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)

        self.reversenums(nums, 0, len(nums)-1)
        self.reversenums(nums, 0, k-1)
        self.reversenums(nums, k, len(nums)-1)


        
# @lc code=end

