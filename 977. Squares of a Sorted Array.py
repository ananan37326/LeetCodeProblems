class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squared = deque()
        l, r = 0, len(nums) - 1
        
        while l <= r:
            left = nums[l] * nums[l]
            right = nums[r] * nums[r]

            if left < right:
                squared.appendleft(right)
                r -= 1
            else:
                squared.appendleft(left)
                l += 1

        return squared
        