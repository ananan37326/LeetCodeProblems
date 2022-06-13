from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []

        res = 1

        for i in range(len(nums)):
            output.append(res)

            res *= nums[i]

        res = 1
        for i in range(len(nums)-1,-1,-1):
            output[i] *= res

            res *= nums[i]

        return output

# test
nums = [-1,1, 0,-3,3]
s = Solution()
print(s.productExceptSelf(nums))
