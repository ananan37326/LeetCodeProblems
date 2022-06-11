from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solution = []
        nums.sort()

        for i, a in enumerate(nums):
            if i>0 and a == nums[i-1]:
                continue
            forwardPtr, reversedPtr = i+1, len(nums)-1

            while forwardPtr < reversedPtr:
                three_sum = a + nums[forwardPtr] + nums[reversedPtr]

                if three_sum > 0:
                    reversedPtr -= 1
                elif three_sum < 0:
                    forwardPtr += 1
                else:
                    solution.append([a, nums[forwardPtr], nums[reversedPtr]])
                    forwardPtr += 1
                    while nums[forwardPtr] == nums[forwardPtr - 1] and forwardPtr < reversedPtr:
                        forwardPtr += 1

        return solution

# TEST

nums = [-1,0,1,2,-1,-4]
s = Solution()
print(s.threeSum(nums))
