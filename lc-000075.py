class Solution:
    def sortColors(self, nums: List[int]) -> None:
        #
        #
        #   Alternative broken solution where I've tried to change the loop invarinat
        #   (come back to this later)
        #

        n = len(nums)
        i, k = 0, n - 1
        j = i

        while i <= j:
            if nums[j] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            elif nums[j] == 2:
                nums[j], nums[k] = nums[k], nums[j]
                k -= 1
                if j >= k: j -= 1
            else:
                if j <= k: j += 1

        return nums


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
                # Maintain A[:i] as an array of 0's
                # - so A[i] may or may not be a 0, we don't care
                # So all indicies from 0, ..., i -1 are zeros (if A[-1] then empty)
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1 # Need to do this increment to maintain i <= j
            elif nums[j] == 2:
                # Maintain A[k + 1:] as array of 2's
                # - A[k] may or may not be a 2, we don't care
                nums[j], nums[k] = nums[k], nums[j]
                k -= 1  # j <= k maintained by loop invariant
            else:
                # A[j] is in the right place
                j += 1  # j <= k maintained by loop invariant

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