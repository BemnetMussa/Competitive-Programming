'''
There are several consecutive houses along a street, each of which has some money inside. There is also a robber, who wants to steal money from the homes, but he refuses to steal from adjacent homes.
The capability of the robber is the maximum amount of money he steals from one house of all the houses he robbed.
You are given an integer array nums representing how much money is stashed in each house. More formally, the ith house from the left has nums[i] dollars.
You are also given an integer k, representing the minimum number of houses the robber will steal from. It is always possible to steal at least k houses.
Return the minimum capability of the robber out of all the possible ways to steal at least k houses.

 

Example 1:

Input: nums = [2,3,5,9], k = 2
Output: 5
Explanation: 
There are three ways to rob at least 2 houses:
- Rob the houses at indices 0 and 2. Capability is max(nums[0], nums[2]) = 5.
- Rob the houses at indices 0 and 3. Capability is max(nums[0], nums[3]) = 9.
- Rob the houses at indices 1 and 3. Capability is max(nums[1], nums[3]) = 9.
Therefore, we return min(5, 9, 9) = 5.
Example 2:

Input: nums = [2,7,9,3,1], k = 2
Output: 2
Explanation: There are 7 ways to rob the houses. The way which leads to minimum capability is to rob the house at index 0 and 4. Return max(nums[0], nums[4]) = 2.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
1 <= k <= (nums.length + 1)/2

--------------------------------------
Given: nums[int] and k: int, can robbe minimum of k houses. it is guranted to robe k houses
    - can't robbe adjuscent houses 
Requested: return the minimum number out of all the possiblites that the robber can steal at least k houses. 
Soltion:    nums = [2,3,5,9, 22, 3, 4, 5, 6], k = 4
                    _                            -> 2 not in the possible ways. 
                      _                          -> 3 not in the possible ways.
                    .......
                   [2,3,5,9], k = 2
                    _        -> 2 not < k
                      -      -> 3 not < k
                        _    -> 5 (2) >= k  --> can be the answer 5
                          -  -> 9 (3) >= k --> can be the answer 9    the answer is 5

            Brute force approch -> O(n^2) 
            optimizaiton
             -> choosing possible capability  ( takes O(N) )-> binary search O(logn) -> O(nlogn)
               min(2) & min(9)
                2, 5
                3 5 i should make it equal. such in that to equal because if it exists then it will count it well that is why
             -> checking part ( takes O(N)) # jump 2 or jump 1

'''
class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:

        left = min(nums)
        right = max(nums)

        def is_valid(capability):
            i = 0
            count = 0

            while i < len(nums):
                if nums[i] <= capability:
                    count += 1
                    i += 2 # jump the adjucent house
                else:
                    i += 1

                if count == k:
                    break

            return count == k

        while left <= right:
            mid = left + (right - left) // 2

            if is_valid(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left