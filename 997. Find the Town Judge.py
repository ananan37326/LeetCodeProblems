class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        incoming = [0] * (n+1)
        outgoing = [0] * (n+1)

        for (a,b) in trust:
            outgoing[a] += 1
            incoming[b] += 1

        for i,v in enumerate(incoming):
            if i==0:
                continue
            if v == n-1 and outgoing[i] == 0:
                return i

        return -1
        