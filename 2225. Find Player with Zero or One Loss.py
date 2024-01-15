from typing import List

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losses_dict = {}
        answers = [[], []]

        for match in matches:
            winner, losser = match

            losses_dict[winner] = losses_dict.get(winner, 0)
            losses_dict[losser] = losses_dict.get(losser, 0) + 1


        for (key, value) in losses_dict.items():
            if value == 0:
                answers[0].append(key)
            elif value == 1:
                answers[1].append(key)

        answers[0].sort()
        answers[1].sort()
        return answers

#Test
matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
print(Solution().findWinners(matches))

        