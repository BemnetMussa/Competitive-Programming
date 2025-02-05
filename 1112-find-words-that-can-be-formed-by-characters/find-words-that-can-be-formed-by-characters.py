class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        

        char_counter = Counter(chars)

        temp = deepcopy(char_counter)
        
        valid = True
        count = 0
        for st in words:
            # hello

            for char in st:
                # h
                if char in char_counter:
                    if char_counter[char] > 0:
                        char_counter[char] -= 1
                    else:
                        valid = False
                        break

                else:
                    valid = False
                    break

            char_counter = deepcopy(temp)

            if valid:
                print(st, valid)
                count += len(st)
      
            valid = True

        return count

            

