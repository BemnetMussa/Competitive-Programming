class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        

        stack = []
        next_map = {}
        for i in range(len(nums2) -1, -1, -1):
         
            while stack and stack[-1] < nums2[i]:
                stack.pop()

            if stack and stack[-1] > nums2[i]:
                next_map[nums2[i]] = stack[-1]
            else:
                next_map[nums2[i]] = -1

            stack.append(nums2[i])

        ans = []
        for num in nums1:
            ans.append(next_map[num])
        print(next_map, ans)
        return ans

        


            