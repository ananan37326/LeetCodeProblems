import random

class RandomizedSet:

    def __init__(self):
        self.val_list = []
        self.index_dict = {}
        

    def insert(self, val: int) -> bool:
        if val in self.index_dict:
            return False
        
        self.val_list.append(val)
        self.index_dict[val] = len(self.val_list) - 1
        return True 
        
        

    def remove(self, val: int) -> bool:
        if val not in self.index_dict:
            return False
        
        last_val = self.val_list[-1]
        index = self.index_dict[val]
        
        self.val_list[index] = last_val
        self.index_dict[last_val] = index
        
        self.val_list.pop()
        self.index_dict.pop(val)
        return True
        

    def getRandom(self) -> int:
        rand_index = random.randint(0, len(self.val_list)-1)
        
        return self.val_list[rand_index]
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()