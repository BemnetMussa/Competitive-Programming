'''
Given tow arrays nums1[int] and nums2[int] of length n.
Rearrange the elements of nums2 such that resulting XOR sum is minimizied 

req: the XOR Sum after the rearrangment to achieve the iminimum XOR sum

Constratins: 1 <= n <= 14. we good

approche: 
what we know is that XOR on the same signals it gives zero. on the different signals it gives one. 
Rearrange nums2 to give nimim XOR sum.

 nums1 = [1,2], nums2 = [2,3]
 First taught -> sort it. and concatenate based on idx's. b/c it will give the correct ones or somallest one every time. hold on we can't rarrange nums1 nice. 

# i won't go too gready on it. because there might be cases that it will might fail based on different inputs. for that case i will consider every single possibleity whcih the approche will be DP

dp approche - > 
    
    using dp approche taking each possiblity and adding it along the way when it reaches the end the total sum tracking it as min one returning it 

'''
class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:

        N = len(nums1)
        # DP - with Bitmasking

        @lru_cache(None)
        def minimumXOR(i, mask):
            if i == N:
                return 0

            min_xor = float("inf")
            for j in range(N):

                if not (mask & (1 << j)):
                    curr_xor = nums1[i] ^ nums2[j]
                    min_xor = min(min_xor, curr_xor + minimumXOR(i+1, mask | (1 << j)))

            return min_xor

        
        return minimumXOR(0, 0)

            







            

        
        