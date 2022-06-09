from typing import List


class Solution:
    def dfs(self, digits, index, path, result, mapping):
        if index == len(digits):
            result.append(path)
            return
        for letter in mapping[digits[index]]:
            self.dfs(digits, index + 1, path + letter, result, mapping)

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        result = []
        self.dfs(digits, 0, "", result, mapping)
        return result


#Test
s = Solution()
print(s.letterCombinations("29"))