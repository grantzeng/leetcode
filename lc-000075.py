class Solution:
    def sortColors(self, nums: List[int]) -> None:


        #
        #   Working solution
        #
        #
        #   Why should the loop invariant be j <= k and not i <= k:
        #   - the first two branchs maintain i <= k: The issue is in third branch
        #     when you increment j it's not guaranteed anywhere else that this will keep j <= k
        #

        n = len(nums)
        i, k = 0, n - 1
        j = i

        while j <= k:
            if nums[j] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            elif nums[j] == 2:
                nums[j], nums[k] = nums[k], nums[j]
                k -= 1
            else:
                j += 1

        return nums

        #
        #
        #   Initial broken attempt
        #   - Dutch flag algorithm
        #
        #   Basically invariants are:
        #   - (i <= j <= k obviously)
        #   - want A[:i] to be 0 (excludes where i is)
        #   - want A[k + 1: ] to be 2?
        #  and we're processing A[i: k]
        #
        # Inspect element at j each time and throw it to either prefix
        # or suffix array

        #
        #   Apparently what's broken about this is i being less than k.
        #   it should be j < k
        #


        n = len(nums)

        i, k = 0, n - 1
        j = i 

        while i <= k: 
            if nums[j] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1 
            elif nums[j] == 2:
                nums[k], nums[j] = nums[j], nums[k]
                k -= 1 
            else: 
                # nums[j] == 1
                j += 1

        return nums