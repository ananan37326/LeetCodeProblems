from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxLen = 0

        for num in nums:
            if num-1 not in numSet:
                length = 0
                while (num+length) in numSet:
                    length += 1
                maxLen = max(maxLen, length)

        return maxLen

#TEST
nums = [0,3,7,2,5,8,4,6,0,1]
s = Solution()
print(s.longestConsecutive(nums))
