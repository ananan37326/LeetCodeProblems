from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        sorted_nums = sorted(nums)
        start = 0
        end = len(nums) - 1
        if nums == sorted_nums:
            return 0
        while start < end:
            if nums[start] != sorted_nums[start]:
                break
            start += 1
        while end > start:
            if nums[end] != sorted_nums[end]:
                break
            end -= 1
        return end - start + 1

#Test
nums = [1,2,3,4]
s = Solution()
print(s.findUnsortedSubarray(nums))