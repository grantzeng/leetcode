class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:

        """
            Going to have a look at 496 to practice monotonic stack

        """
        
        """
            2024-05-30
            First attempt/researching intuition of how this work

            C(n, 2) subarrays so bruteforce is O(n^2)

            For subarray A[i, j] inclusive we want i, j s.t. 

            L = max ((min A[i,j] * sum A[i, j]) % (10^9 + 7))
            is maximised. 

            Problem: Want a O(n) algorithm to do this
            
            Overall strategy for the "usual" solution.
            - you need to know about monotonic stacks and prefix sums (neither of which you did)
            - map A[k] to its corresponding min product
                - for each A[k] find the window/A[i:j] for which it is the minimal element
                  - (this is what is giving you grief, because not sure how monotonic stack helps here)
                  - prefix sums useful for computing subarray sum in O(1)
            - then O(n) search for the maximum

            This code is broken
        """

        n = len(nums)
        prefix_sum = [ sum(nums[0:i + 1]) for i in range(n) ]  # so sum A[i,j] = prefix_sum[j] - prefix_sum[i]
        left_bound = [ i for i in range(n) ]                   # we know A[k] will be minimal in the single element subarray A[k:k]
        right_bound = [ i for i in range(n) ]
        
        
        stack = []
        for i in range(n): 
            while stack and nums[stack[-1]] > nums[i]: 
                stack.pop()
            left_bound[i] = stack[-1] if stack else i #
            stack.append(i)

        stack = []

        for j in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] > nums[j]: 
                stack.pop()
            right_bound[j] = stack[-1] if stack else j #
            stack.append(j)

        return min(nums[k] *(prefix_sum[right_bound[k]]) - prefix_sum[left_bound[k]] for k in range(n))
         
