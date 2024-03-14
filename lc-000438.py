class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        #
        #   An optimized soltuion
        #
        #
        #

        #
        #   An obvious solution
        #   - we have a window of size len(p)
        #   - anagram -> they have the same "spectrum" in the sense two words have same letter frequencies
        #
        #   The main issue with this one is you recompute the frequency table every time you shift the window
        #   which isn't great if p is very long.
        """
        from collections import Counter 
        idxs = []  

        freq_p = Counter(p)

        i, j = 0, len(p) - 1
        while j < len(s): 
            if Counter(s[i:j + 1]) == freq_p: 
                idxs.append(i)

            i, j = i + 1, j + 1

        return idxs
        """