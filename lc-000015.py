class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #
        #   TODO: How to do this WITHOUT sorting input (e.g. pay for some space)
        #
        #

        #
        #   TODO: Optimize the O(1) (excluding writing down all the triples)
        #         to avoid all the set membership checks by skipping repeated elements
        #

        #
        #   3SUM purely pointer based solution (other than set that keeps track
        #   of triplets
        #
        #   - Deal with the solution first which is. Repeat 2SUM problem on f
        #

        # Pointer based solution needs input sorted otherwise how to tell
        # which way to move a pointer to increase/decrease intermediate sums
        nums.sort()

        res = []
        n = len(nums)

        # Fix choice of prefix array/A[i: ]
        for i in range(n - 2):

            # For prefix array, repeat the two sum problem
            j = i + 1
            k = n - 1

            targ = -nums[i]
            while j < k:
                tot = nums[j] + nums[k]

                if tot < targ:
                    j += 1
                elif tot > targ:
                    k -= 1
                else:
                    trip = (nums[i], nums[j], nums[k])
                    if trip not in res:
                        res.append(trip)
                    j += 1
                    k -= 1

            return res

        """
            Recapping 2SUM
            - Doesn't work for original 2SUM problem because it asks for
              indices for elements that add to target, not just values
              (the sort messes up the original ordering)
        """
        # nums.sort()
        # i, j = 0, len(nums) - 1

        # while i <= j:
        #     s = nums[i] + nums[j]

        #     if s > target:
        #         # Overshoot, reduce upper bound
        #         j -= 1
        #     elif s < target:
        #         # Undershoot, raise lower bound
        #         i += 1
        #     else:
        #         # Found match
        #         return (nums[i], nums[j])
                
