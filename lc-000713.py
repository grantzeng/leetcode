class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:


        """
            The issue was where you put the update to counting the subarrays
            - See note below.
            - Basically we try to multiplty nums[j] then check if it broke an invariant and fix it

            Why does increment go last? We don't know if multipltying nums[j] will break invariant
            of subarray product being less than k. So better to check and fix that first.
        """
        i, j = 0, 0

        res = 0

        prod = 1
        while j < len(nums):
            prod *= nums[j]

            while prod >= k and i <= j:
                prod /= nums[i] if nums[i] != 0 else 1
                i += 1

            # if A[i:j] has a product less than k, then so do all A[i:x] where x < j
            # - Basically, you were under counting.
            res += j - i + 1
            j += 1

        return res

        """
            Initial broken solution that undercounts the number of subarrays
            - Basically need to somehow maintain some kind of subarray variable
        """
        i, j = 0, 0 
        
        res = 0 

        prod = 1
        while j < len(nums): #
            prod *= nums[j]

            if prod < k: res += 1 # This undercounts

            while prod >= k and i <= j:
                prod /= nums[i] if nums[i] != 0 else 1
                i += 1    

            j += 1

        return res