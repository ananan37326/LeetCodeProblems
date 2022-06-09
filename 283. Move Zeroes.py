from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last_non_zero = 0

        for i in range (len(nums)):
            if nums[i] != 0:
                nums[last_non_zero] = nums[i]
                last_non_zero += 1

        for i in range(last_non_zero,len(nums)):
            nums[i] = 0


# TEST
nums = [0,0,0,0,1]
s = Solution()
s.moveZeroes(nums)
print(nums)
