class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq = Counter(arr)

        freqCount = [0] * (len(arr) + 1)

        for n, f in freq.items():
            freqCount[f] += 1

        res = len(freq)

        for f in range(1, len(freqCount)):
            remove = freqCount[f]

            if k >= f*remove:
                k -= f*remove
                res -= remove
            else:
                remove = k // f
                res -= remove
                break
        
        return res