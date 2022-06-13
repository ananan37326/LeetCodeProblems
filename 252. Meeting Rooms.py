from typing import List

class Solution:

    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals = sorted(intervals,key=lambda x:x[0])

        for i in range(len(intervals)-1):
            if intervals[i][1] >intervals[i+1][0]:
                return False

        return True

# TEST
nums = [[0,4],[5,10],[15,20]]
s = Solution()
print(s.canAttendMeetings(nums))

