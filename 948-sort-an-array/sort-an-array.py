class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(left_val, right_val):
            left = 0
            right = 0

            merge = []

            while left < len(left_val) and right < len(right_val):
                if left_val[left] < right_val[right]:
                    merge.append(left_val[left])
                    left += 1
                else:
                    merge.append(right_val[right])
                    right += 1

            while left < len(left_val):
                merge.append(left_val[left])
                left += 1
            
            while right < len(right_val):
                merge.append(right_val[right])
                right += 1

            return merge

        def mergeSort(left, right, arr):
            if left == right:
                return [arr[left]]

            mid = left + (right - left) // 2

            left_val = mergeSort(left, mid, arr)
            right_val = mergeSort(mid+1, right, arr)

            return merge(left_val, right_val)

        return mergeSort(0, len(nums)-1, nums)
            
                

            #[1,2,3] [2,3,4]
            #[1, ]