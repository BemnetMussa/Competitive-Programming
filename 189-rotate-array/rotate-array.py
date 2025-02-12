class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Rotate the array to the right by k steps in place.
        """
        k = k % len(nums)
        first = nums[-k:]

        second = nums[:-k]

        nums[:] = first + second


   