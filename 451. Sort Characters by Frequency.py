class Solution:
    def frequencySort(self, s: str) -> str:
        freq = defaultdict(int)
        bucket = defaultdict(list)
        res = ""

        for ch in s:
            freq[ch] += 1

        for ch, count in freq.items():
            bucket[count].append(ch)

        for i in range(len(s), 0, -1):
            for c in bucket[i]:
                res += (c*i)

        return res