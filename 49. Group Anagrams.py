class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for str in strs:
            count = [0] * 26
            
            for c in str:
                count[ord(c) - ord('a')] += 1

            res[tuple(count)].append(str)

        return res.values()
        