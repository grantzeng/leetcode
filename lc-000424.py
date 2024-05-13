class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        """
            Working solution.

            O(n^2) because the window inching is O(n). But lookup for the max-value
            is O(n) as well because we basically only have a list.

            The invariant that subarray has to satisfy is that it can't have
            more than k non-mode letters. We _update_ the left bound to fix violation
            of the invariant caused by greedily extending right bound
        """
        n = len(s)
        i, j = 0, 0
        res = 0
        seen = {}

        while j < n: # Keep trying to expand right bound
            ch = s[j]
            seen[ch] = seen.get(ch, 0) + 1

            # Logic for contracting the window
            # - There are MORE than k letters we'd have to replace
            while (j - i + 1) - max(seen.values()) > k:
                seen[s[i]] -= 1
                i += 1

            # Tracking subarray lengths
            res = max(res, j - i + 1)
            j += 1

        return res


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
