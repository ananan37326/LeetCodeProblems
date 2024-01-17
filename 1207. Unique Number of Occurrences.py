class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arr_dict = {}
        occur_set = set()

        for num in arr:
            arr_dict[num] = arr_dict.get(num, 0) + 1

        for (key, val) in arr_dict.items():
            if val in occur_set:
                return False
            occur_set.add(val)

        return True