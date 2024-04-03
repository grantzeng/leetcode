class Solution:
    def countGoodSubstrings(self, s: str) -> int:

        #
        # Initial solutio
        #   - Could optimize this by not rebuilding set every window step
        #
        n = len(s)
        k = 3 

        good = 0 
        for i in range(n - k + 1):

            if len(set(list(s[i:i+k]))) == k: 
                # Three distinct characters
                good += 1
        
        return good