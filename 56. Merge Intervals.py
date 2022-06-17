from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2 :
            return intervals


        intervals.sort(key=lambda x:x[0])
        output = [intervals[0]]

        for start, end in intervals[1:]:
            if output[-1][1] >= start:
                output[-1][1] = max(output[-1][1],end)
            else:
                output.append([start,end])

        return output

# TEST

intervals = [[1,4],[0,4]]
s = Solution()
print(s.merge(intervals))
