class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        minus, minus_sq = 0, 0
        for i in range(1, len(nums)+1):
            minus += (nums[i-1] - i)
            minus_sq += (nums[i-1]**2 - i**2)
        
        plus = minus_sq//minus
        return [(plus+minus)//2, (plus-minus)//2]
        