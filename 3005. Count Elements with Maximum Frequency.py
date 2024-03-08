class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freqs = defaultdict(int)
        total_freq = max_freq = 0

        for num in nums:
            freqs[num] += 1

            if freqs[num] > max_freq:
                max_freq = freqs[num]
                total_freq = freqs[num]
            
            elif freqs[num] == max_freq:
                total_freq += max_freq

        return total_freq
        