class Solution:
    def compress(self, chars: List[str]) -> int:
        '''
        Things to keep track of 
            - writer (pointer): where we write
            - reader (pointer): scans the array
            - counter (count the frequencies)
            - current (character that is been counted)
        '''

        N = len(chars)
        writer = 0
        reader = 0

        while reader < N:
            current = chars[reader]
            count = 0

            # count char frequency 
            while reader < N and chars[reader] == current:
                reader += 1
                count += 1

            # write character 
            chars[writer] = current
            writer += 1

            if count > 1:
                for digits in str(count):
                    chars[writer] = digits
                    writer += 1
                   
        return writer # lenth of valid compressed array 
            