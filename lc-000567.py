class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        #
        #   Try reimplement the optimized solution but make it readable
        #   - But I think this doesn't work well because inherently you're working at the level of
        #     an array and not at some higher abstraction. So the code is just not going to look nice
        #

        n, m = len(s1), len(s2)
        if n > m: return False

        targ, wind = [0] * 26, [0] * 26

        ordinal = lambda s, i: ord(s[i]) - ord('a') # Discouraged to use lambdas like this?

        # Populate frequency and initial value of match "statistic"
        # - Match is basically a sum of indicator functions
        for i in range(n):
            targ[ordinal(s1, i)] += 1
            wind[ordinal(s2, i)] += 1

        matches = sum(1 if targ[i] == wind[i] else 0 for i in range(26))

        # Sliding window and updating the window frequency table
        for l, r in zip(range(m - n + 1), range(n, m)):
            if matches == 26:
                # Found the window, kill program
                return True
            else:
                # Update frequency table for window
                #  - Remove left from window and update matches
                idx = ordinal(s2, l)
                wind[idx] -= 1

                if wind[idx] == targ[idx]:          matches += 1
                elif wind[idx] + 1 == targ[idx]:    matches -= 1

                #  - Add right to window and update matches
                idx = ordinal(s2, r)
                wind[idx] += 1

                if wind[idx] == targ[idx]:          matches += 1
                elif wind[idx] - 1 == targ[idx]:    matches -= 1

        return matches == 26    # There is one last equality check we didn't do


        #
        #   To be honest, the actually maintainable solution is just to pay for the set equality check
        #
        """
        from collections import Counter
        n, m = len(s1), len(s2)

        if n > m: return False
        targ, wind = Counter(s1), Counter(s2[:n])

        # Sliding window
        for l, r in zip(range(m - n + 1), range(n, m)):
            print(targ, wind)
            if targ == wind:
                # Sitting on a window which is a permutation
                return True
            else:
                # Update window's frequnecy table
                wind[s2[l]] -= 1
                wind[s2[r]] += 1

        return targ == wind
        """
        #
        # Trying again to implement C style solution
        # - Basically, don't want:
        #       - O(s1 * s2) solution - which happens if you rebuild frequency table every time it slides
        #         when you use Counter
        #       - O(26 * s2) solution - from having loop through to check equality of letter frequency tables
        # - Reduce this to O(s1) solution with O(1) space of the 'matches' variable that is like statistic
        #   on whether the two frequency tables are equal or not
        #
        # this is basically the solution neetcode gives but with some syntactic sugar. It's...fast
        """
        n, m = len(s1), len(s2)
        if n > m: return False

        targ, wind = [0] * 26, [0] * 26
        for i in range(n):
            targ[ord(s1[i]) - ord('a')] += 1
            wind[ord(s2[i]) - ord('a')] += 1

        matches = sum([
            1 if targ[i] == wind[i] else 0
            for i in range(26)
        ])

        # Sliding window
        for l, r in zip(range(0, m - n), range(n, m)):
            # print(targ)
            # print(wind)
            # print(matches)
            # print(s1)
            # print(s2[l:r])
            # print()
            if matches == 26: return True

            # Remove left character from window
            idx = ord(s2[l]) - ord('a')
            wind[idx] -= 1

            if   targ[idx] == wind[idx]:        matches += 1        # New match
            elif targ[idx] - 1 == wind[idx]:    matches -= 1        # Caused mismatch

            # Add right character to window
            idx = ord(s2[r]) - ord('a')
            wind[idx] += 1

            if   targ[idx] == wind[idx]:        matches += 1        # New match
            elif targ[idx] + 1 == wind[idx]:    matches -= 1        # Caused mismatch


        return matches == 26
        """

        #
        #
        #   Improved solution that uses a match count so I only have to pay O(1)
        #   to check frequency table equality.
        #
        #   Couldn't make this work, I think you should use a dict
        #
        """
        # Set up letter frequency tables for target string and window
        window_size, target_size = len(s1), len(s2)
        if target_size < window_size:
            return False

        target_freqs = [0] * 26
        window_freqs = [0] * 26

        for i in range(window_size):
            target_freqs[ord(s1[i]) - ord('a')] += 1
            window_freqs[ord(s2[i]) - ord('a')] += 1

        # "Checksum" for checking if the two tables
        matching = sum(1 if s1[i] == s2[i] else 0 for i in range(window_size))

        #

        # Sliding window

        for l, r in zip(
            range(target_size - window_size + 1),
            range(window_size, target_size)
        ):
            if matching == 26:
                # Frequency tables matching
                return True

            # Remove left character of window from frequency table
            # - Update if changed matching state
            idx_left = ord(s2[l]) - ord('a')
            window_freqs[idx_left] -= 1
            if window_freqs[idx_left] ==target_freqs[idx_left]:
                matching +=1
            elif window_freqs[idx_left] + 1 == target_freqs[idx_left]:
                matching -= 1

            # Add right character to frequency table
            idx_right = ord(s2[r]) - ord('a')
            window_freqs[idx_right] += 1
            if window_freqs[idx_right] == target_freqs[idx_right]:
                matching += 1
            elif window_freqs[idx_right] - 1 == target_freqs[idx_right]:
                matching -= 1
        return False if matching != 26 else True
        """
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
            # Update for right bound
            window[x] += 1

            # Update for left bound, if window has grown to full size and is shifting
            if i >= len(s1): window[B[i - len(s1)]] -= 1

            if window == target:
                # Frequnecy table of current window is same as target, return
                # Problem: this costs O(26)
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

s1 = 'ab'
s2 = 'eidbaooo'

print(Solution().checkInclusion(s1, s2))