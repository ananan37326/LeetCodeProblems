from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        total = 0
        start = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if total < 0:
                start = i + 1
                total = 0
        return start

# test
gas = [2,3,4]
cost = [3,4,3]
s = Solution()
print(s.canCompleteCircuit(gas, cost))
