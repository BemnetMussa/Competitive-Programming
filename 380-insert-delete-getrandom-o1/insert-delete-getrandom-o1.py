class RandomizedSet:

    def __init__(self):
        self.dict_index = defaultdict(int)
        self.arr = []
                                                 
        

    def insert(self, val: int) -> bool:
        if val in self.dict_index:
            return False
    
        self.arr.append(val)
        self.dict_index[val] = len(self.arr) - 1

        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.dict_index:
            return False

        # getting the index the value
        index_val = self.dict_index[val]
        # swap val to the last arr
        self.swap(index_val, -1)

        # poping the last 
        self.arr.pop()
        del self.dict_index[val]
        return True
        
    
    def swap(self, val_index, last_index):
        temp = self.arr[val_index]
        self.arr[val_index] = self.arr[last_index]
        self.arr[last_index] = temp

        # update the index of the swaped val
        self.dict_index[self.arr[val_index]] = val_index


    def getRandom(self) -> int:
        return random.choice(self.arr)







# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()