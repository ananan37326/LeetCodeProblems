from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}
        for i in nums:
            if hashmap.get(i) is not None:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
            if hashmap[i] > len(nums)//2:
                return i


# TEST
nums = [2,4,4,1,4,3,4,6,4]
s = Solution()
print(s.majorityElement(nums))