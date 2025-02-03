class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        # each interval between [left, right] must be included 
        # find at least one itnerval in ragnes that staisfies the above condition

        """
            range = [[1,2],[3,4],[5,6]], left = 2, right = 5
                      | |                   for this only 2 is included
                            | |             between 2 and 5 is included exlsive 
                                  | |       for this only 5 is included 
            so all of the numbers between left and right inclusive are included within the ragne so 
            return True

            approch 

                num = [x for x in range(left, right + 1)]
                # [2, 3, 4 , 5]
                
                for range in ranges:
                    # 1, 2
                    for v in range(range[0], range[1] +1):
                        # 1, 2 in num                           # [3, 4, 5]
                        # 3, 4 in num                           # [5]
                        # 5, 6 in num                           # []
                        if v in num:
                            num.remove(v)

                # num = []
                return True if num == [] else False

            

        """
 
        num = [x for x in range(left, right + 1)]
            
        for ra in ranges:
            for v in range(ra[0], ra[1] +1):
                if v in num:
                    num.remove(v)

        print(num)

        return True if num == [] else False

        