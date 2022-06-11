from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        forwardPtr = 0
        reversePtr = len(numbers) - 1
        while True:
            sum = numbers[forwardPtr] + numbers[reversePtr]
            if sum == target:
                return [forwardPtr+1,reversePtr+1]
            elif sum < target:
                forwardPtr += 1
            else :
                reversePtr -= 1


# TEST
numbers = [-1,0]
target = -1
s = Solution()
print(s.twoSum(numbers,target))
