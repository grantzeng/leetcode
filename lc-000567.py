class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        #
        #   Basically, I get how to make the sliding window work
        #   the issue is setting up a dictionary that I can edit each time
        #
        #   - Broken solution, need to fix
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
        for l, r in zip(range(whole - window), range(window, whole)):

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






        #
        #   This solution works but it's no longer O(n) because
        #   you pay O(n) every time you rebuild frequency table
        #   - Better to keep a table that you update as you go
        #     or the trick of using 26 element long array for each letter
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

