import collections
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squaredList = collections.deque()

        forwardPtr = 0
        reversePtr = len(nums) - 1

        for i in range(len(nums)):
            if abs(nums[forwardPtr]) < abs(nums[reversePtr]):
                squaredList.appendleft(nums[reversePtr]*nums[reversePtr])
                reversePtr -= 1
            else:
                squaredList.appendleft(nums[forwardPtr]*nums[forwardPtr])
                forwardPtr += 1
        return list(squaredList)


# TEST
nums = [-4,-3,0,1,2]
s = Solution()
print(s.sortedSquares(nums))
