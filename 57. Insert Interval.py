from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        output = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                output.append(newInterval)
                return output + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                output.append(intervals[i])
            else:
                newInterval = [min(newInterval[0],intervals[i][0]),max(newInterval[1],intervals[i][1])]

        output.append(newInterval)

        return output


# TEST
intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]

s = Solution()
print(s.insert(intervals,newInterval))
