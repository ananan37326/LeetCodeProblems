from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_set = set(nums.copy())

        return len(nums) != len(num_set)


# TEST
nums = [1,2,3,4,1]
s = Solution()
print(s.containsDuplicate(nums))
