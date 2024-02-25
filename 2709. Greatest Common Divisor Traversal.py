class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n
        self.count = n

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)

        if px == py:
            return

        if self.rank[px] < self.rank[py]:
            self.par[px] = py
            self.rank[py] += self.rank[px]
        else:
            self.par[py] = px
            self.rank[px] += self.rank[py]
        self.count -= 1

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        uf = UnionFind(len(nums))

        factors = {}

        for i, n in enumerate(nums):
            f = 2
            while f*f <= n:
                if n % f == 0:
                    if f in factors:
                        uf.union(factors[f], i)
                    else:
                        factors[f] = i
                    
                    while n%f == 0:
                        n //= f
                f += 1
            
            if n > 1:
                if n in factors:
                    uf.union(factors[n], i)
                else:
                    factors[n] = i
        return uf.count == 1
        