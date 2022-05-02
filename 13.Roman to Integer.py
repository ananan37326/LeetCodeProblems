class Solution:
    # method to convert roman numeral to integer
    def romanToInt(self, s: str) -> int:
        # dictionary to store roman numerals and their corresponding integer values
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        # initialize sum to 0
        sum = 0

        # iterate through the string
        for i in range(len(s)):
            # if the current character is smaller than the next character, subtract the current character's value
            # from the sum
            if i < len(s) - 1 and roman_dict[s[i]] < roman_dict[s[i + 1]]:
                sum -= roman_dict[s[i]]
            # otherwise, add the current character's value to the sum
            else:
                sum += roman_dict[s[i]]

        return sum


# test cases
s = Solution()
print(s.romanToInt("IV"))
