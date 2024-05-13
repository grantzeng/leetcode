class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        """
            I think two while loops makes more sense because we're controlling array bounds with two
            "pointers" but this is the for loop solution instead

            TODO: Rewrite with defaultdict so it handles the resource checks
        """

        res = 0
        i = 0
        seen = {}

        for j in range(len(s)):
            seen[s[j]] = seen.get(s[j], 0) + 1
            while seen[s[j]] > 1:
                seen[s[i]] -= 1
                i += 1
            res = max(j - i + 1, res)

        return res

        """
            Actually we didn't need that if statement at all, because the while loop is checking for it anyway!
        """

        res = 0
        i, j  = 0, 0
        seen = {}
        while j < len(s):   # Expand right bound
            ch = s[j]
            seen[ch] = seen.get(ch, 0) + 1


            while seen[ch] > 1: # Contract left bound until fix invariant
                seen[s[i]] -= 1
                i += 1

            res = max(j - i + 1, res)
            j += 1

        return res

        """
            Better O(n) solution where you have two loops controlling
            - single set object tracking letters in current subarray that you modify

            Inspiration is from 209.

            I think it's _sort_ of greedy. i.e. we want longest window, so keep trying to extend it
            until some invariant is violated, then contract until the invariant is fixed? (Invariant
            being that valid window has no repeats)

        """
        n = len(s)
        res = 0

        i, j = 0, 0
        seen = {}

        while j < n: # Greedily try to expand the window
            ch = s[j]
            seen[ch] = seen.get(ch, 0) + 1

            if seen[ch] > 1:
                # Saw a repeat, naively keep deleting left bound
                # until no repeats
                while seen[ch] > 1:
                    seen[s[i]] -= 1
                    i += 1

            res = max(j - i + 1, res) # Snapshot window length
            j += 1

        return res



        """
            Basic working solution:
            - but kinda slow because of how I rebuild set every time?

        """
        n = len(s)
        max_length = 0
        
        for i in range(n):
            window = set()
            for char in s[i:]:
                if char in window: break
                window.add(char)
            max_length = max(max_length, len(window))

        return max_length

        """
            Almost works,
            but you already added start character...so maybe don't do that

        """

        n = len(s)
        max_length = 0

        for i, start in enumerate(s):
            window = set([start])
            for char in s[i:]:
                if char in window:
                    break
                window.add(char)
            max_length = max(max_length, len(window))

        return max_length

        """
            Initial attempts:
            - Some strange off by one errors? Not that strang see note below

            - Basically you have a variable sized window, it should
              grow until you find a repeated character, at which point
              you restart the window?

            This algorithm doesn't work because it only restarts the window
            at positions that is a repeated charater
            e.g. for "dvdf" it won't check for any window starting at v!

        """
        window = set()
        max_length = 0 
        
        for char in s: 
            if char in window: 
                window = set()
            window.add(char)
            max_length = max(max_length, len(window))

        return max_length

        # window = set()
        # max_length = 0 
        
        # for char in s: 
        #     if char in window: 
        #         window = set()
        #     max_length = max(max_length, len(window))
        #     window.add(char)

        # return max_length