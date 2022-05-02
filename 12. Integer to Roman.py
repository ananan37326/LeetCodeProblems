class Solution:
    def intToRoman(self, num: int) -> str:
        roman = ''
        roman_dict = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}

        while num > 0:
            for i in roman_dict:
                if num >= i:
                    roman += roman_dict[i]
                    num -= i
                    break

        return roman


#Test
s = Solution()
print(s.intToRoman(1994))