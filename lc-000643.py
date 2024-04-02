class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        #
        #   This one works
        #   - Expected behaviour when input is smaller than windo
        #     is just to add everything up?
        #
        #   Time: O(n)
        #   Space: O(1) since only two variables to store sums
        #
        n = len(nums)
        window_sum = max_sum = sum(nums[:k])
        for i in range(k, n):
            window_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, window_sum)

        return max_sum / k


        #
        # Sliding window but specifing the two pointers explicitly
        #  rather than using sliding
        # - This also breaks when the array is less than size k.
        #
        n = len(nums)

        # Pointers for sliding window
        # - j is left as k - 1 because I want j to always refer to a valid index
        #   but this convention will force you to add a + 1 when doing array slicing
        #   because in Python the upper bound is exclusive
        i, j = 0, k - 1

        # Initialise estimate as zero
        # - Since subarray size is fixed, we only divide by a constant factor 
        #   to get the average (i.e. it's just rescaling all the possible window
        #   averages and doesn't change their relative positions) so just ignore it
        best_total = 0

        # Slide the size k-window until right edge hits end of array
        # - calculate sum on this window and update estimate
        while j < n: 
            window_total = sum(nums[i:j + 1])
            best_total = max(best_total, window_total)
            i, j = i + 1, j + 1

        return best_total / k


        #
        # This one tries to combine the window growing to size k
        # - but it doesn't work because of issues with reporting
        #   the highest number when within the first k.
        #
        n = len(nums)
        window_sum = 0
        max_sum = float('-inf')
        for i in range(n):

            if i < k:
                window_sum += nums[i]
            else:
                window_sum += nums[i]
                window_sum -= nums[i - k]

            max_sum = max(max_sum, window_sum)

        return max_sum / k

