class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
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