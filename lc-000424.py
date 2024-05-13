class Solution:
    def characterReplacement(self, s: str, k: int) -> int:


        """
            Initial attempt:
            - Basic variable length sliding window set up
              (but not sure what condition should be for updating left bound)
        """
        
        n = len(s)
        i, j = 0, 0 

        # Greedily try to expand right bound of window
        while j < n:

            # If violation of invariant, keep contracting left bound
            # until invariant is fixed? ()

            #
            #   ???? What is the invariant to put here ???
            #

            # Tracking subarray lengths
            res = max(res, j - i + 1) 
            j += 1

        return res
