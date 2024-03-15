class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:


        #
        #   Working solution
        #   - But stil am checking array equality rather than using a helper variable
        #
        #   TODO: Implement having a match variable to check if states the same
        #

        # Populate frequency table of target
        target = [0] * 26
        for x in [ord(c) - ord('a') for c in s1]: target[x] += 1

        # Sliding window: load frequency table then update when bigger than window
        window = [0] * 26
        B = [ord(c) - ord('a') for c in s2]

        for i, x in enumerate(B):
            # Update right bound
            window[x] += 1

            # Update left bound, if window has grown to full size and is shifting
            if i >= len(s1): window[B[i - len(s1)]] -= 1

            if window == target:
                # Frequnecy table of current window is same as target, return
                return True


        return False

        #
        #   Broken solution trying to implement having a match variable to keep track
        #   of whether two frequency tables explicitly the same
        #

        """
        if len(s1) > len(s2): return False

        window, whole = len(s1), len(s2)
        f1, f2 = [0] * 26, [0] * 26

        # Return indexes to make updating frequency tables easier
        idx = lambda s, i: ord(s[i]) - ord('a')

        for i in range(window):
            f1[idx(s1, i)] += 1
            f2[idx(s2, i)] += 1

        # Sliding window with updates to matches
        match = sum(1 if f1[i] == f2[i] else 0 for i in range(26))
        for l, r in zip(range(whole - window + 1), range(window, whole)):

            # Previous window matched up completely
            if match == 26: return True

            # Update tables for left of window
            i1 = idx(s2, l)
            f2[i1] -= 1

            if f2[i1] == f1[i1]:        match += 1
            elif f2[i1] - 1 == f1[i1]:  match -= 1

            # Update tables for right of window
            i2 = idx(s2, r)
            f2[i2] -= 1
            if f2[i2] == f1[i2] :       match += 1
            elif f2[i2] + 1 == f1[i2]:  match -= 1

        return False
        """

        #
        #   Working naive solution but is suboptimal because we're
        #   rebuilding an entire frequency table each window step
        #   rather than just updating it
        #
        """
        from collections import Counter 
        
        c2 = Counter(s1)

        for i in range(len(s2) - len(s1) + 1): 
            c = Counter(s2[i:i + len(s1)])
            if c == c2:
                return True 
        return False
        """

