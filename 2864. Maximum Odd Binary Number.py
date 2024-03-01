class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        oneCount = s.count("1")

        return "1" * (oneCount - 1) + "0" * (len(s) - oneCount) + "1"
        