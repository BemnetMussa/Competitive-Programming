class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """


        target = Counter(p)

        ans = []
        k = len(p)-1

        check = Counter(s[:k])

        for i in range(k, len(s)):

    
            if s[i] in check:
                check[s[i]] += 1
            else:
                check[s[i]] = 1

            if check == target:
                ans.append(i-k)

            check[s[i-k]] -= 1
            if check[s[i-k]] == 0:
                del check[s[i-k]]
       


        return ans