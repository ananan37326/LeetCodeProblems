from typing import List


class Solution:
    #In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.
    def maxOperations(self, nums: List[int], k: int) -> int:
        numDict = {}
        for num in nums:
            numDict[num] = numDict.get(num,0) + 1

        count = 0
        for num in numDict:
            if num == k-num:
                if numDict.get(num,0) > 1:
                    count += (numDict.get(num,0))//2
                    numDict[num] -= (numDict.get(num,0))//2 * 2
            else:
                if numDict.get(k-num,0) > 0:
                    minOcc = min(numDict.get(num,0), numDict.get(k-num,0))
                    count += minOcc
                    numDict[k-num] -= minOcc
                    numDict[num] -= minOcc

        return count

#Test
nums = [4,4,1,3,1,3,2,2,5,5,1,5,2,1,2,3,5,4]
k = 9
print(Solution().maxOperations(nums,k))