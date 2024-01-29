class FrequencyTracker:

    def __init__(self):
        self.vals = defaultdict(int)
        self.freq = defaultdict(int)
        

    def add(self, number: int) -> None:
        old_freq = self.vals[number]

        if old_freq > 0:
            self.freq[old_freq] -= 1
        
        self.vals[number] += 1

        new_freq = self.vals[number]
        self.freq[new_freq] += 1
        
        

    def deleteOne(self, number: int) -> None:
        old_freq = self.vals[number]

        if old_freq > 0:
            self.freq[old_freq] -= 1
            self.vals[number] -= 1

            new_freq = self.vals[number]
            self.freq[new_freq] += 1
        

    def hasFrequency(self, frequency: int) -> bool:
        return self.freq[frequency] > 0
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)