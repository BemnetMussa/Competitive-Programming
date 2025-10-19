class RandomizedSet:
    def __init__(self):
        self.store = []
        self.map_index = {}

    def insert(self, val: int) -> bool:
        if val in self.map_index:
            return False

        self.store.append(val)
        self.map_index[val] = len(self.store) - 1

        return True


    def remove(self, val: int) ->  bool:
        if val not in self.map_index:
            return False
        
        last_indx = len(self.store) - 1
        val_index = self.map_index[val]

        self.store[last_indx], self.store[val_index] = self.store[val_index], self.store[last_indx]
        
        self.map_index[self.store[val_index]]  = val_index

        del self.map_index[val]
        self.store.pop()

        return True

    def getRandom(self) -> int:
        index = random.randint(0, len(self.store) - 1)
        return self.store[index]

