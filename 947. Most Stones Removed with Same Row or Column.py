from typing import List


class Solution:
    def find(self, x, parent):
        if parent[x] != x:
            parent[x] = self.find(parent[x], parent)
        return parent[x]


    def union(self, x, y, rank, parent):
        x_parent = self.find(x, parent)
        y_parent = self.find(y, parent)

        if x_parent != y_parent:
            if rank[x_parent] > rank[y_parent]:
                parent[y_parent] = x_parent
                rank[x_parent] += rank[y_parent]
            else:
                parent[x_parent] = y_parent
                rank[y_parent] += rank[x_parent]
        return parent, rank



    def removeStones(self, stones: List[List[int]]) -> int:
        count = 0
        n = len(stones)
        parent = [i for i in range(n)]
        rank = [1 for _ in range(n)]

        for i in range(n):
            for j in range(i+1, n):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    self.union(i, j, rank, parent)

        for i in range(n):
            if parent[i] ==i:
                count += 1

        return n - count


#Test
s = Solution()
print(s.removeStones([[0,0],[0,2],[1,1],[2,0],[2,2]]))


