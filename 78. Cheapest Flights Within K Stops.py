class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [math.inf] * (n)
        prices[src] = 0

        for _ in range(k+1):
            tmpPrices = prices.copy()
            for s, d, p in flights:
                if prices[s] == math.inf:
                    continue

                if prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p

            prices = tmpPrices

        return -1 if prices[dst]==math.inf else prices[dst]
        