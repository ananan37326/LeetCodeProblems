import math
from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        stack = []

        mid_num = -math.inf
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < mid_num:
                return True
            while stack and nums[i] > stack[-1]:
                mid_num = stack.pop()
            stack.append(nums[i])
        return False

#test
nums = [1, 2, 5, 4]
s = Solution()
print(s.find132pattern(nums))

