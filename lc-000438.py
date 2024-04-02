class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        #
        #   Optimized solution using 26-element long "array" instead of a hash table
        #   - the C-style solution
        #
        #
        
        targ, wind = [0] * 26, [0] * 26
        anagram_idxs = []

        # TODO: Come back to this

        return anagram_idxs

        #
        #   Trying to come up with a solution where we update the window frequency table each step
        #   - This doesn't work because there's an off by 1 error because we don't check frequnecy table
        #     in last iteration of the loop
        #
        #   Time: O(|s| + |p|) due to cost of building initially (looping through is just O(|p|)
        #   Space: O(1) because there's only at most 26 key-value pairs for both tables
        #
        from collections import Counter
        window_size, n = len(p), len(s)
        target, window = Counter(p), Counter(s[:window_size])

        anagram_idxs = []

        for i in range(n - window_size):

            if window == target:
                anagram_idxs.append(i)

            window[s[i + window_size]] += 1
            window[s[i]] -= 1

        if window == target:
            anagram_idxs.append(n - window_size)

        return anagram_idxs


        #
        #   This now works, issue was an off by 1 error of the window
        #   - But is slow because we rebuilding the window char frequency table each time (but this is
        #     still a constant time operation because window is fixed size, I think)
        #
        from collections import Counter
        target = Counter(p)

        anagram_idxs = []

        window_size = len(p)
        n = len(s)
        for i in range(n - window_size + 1):
            window = Counter(s[i:i + window_size])
            print(s[i: i + window_size])

            if window == target:
                anagram_idxs.append(i)

        return anagram_idxs

        #
        #   An obvious solution
        #   - we have a window of size len(p)
        #   - anagram -> they have the same "spectrum" in the sense two words have same letter frequencies
        #
        #   The main issue with this one is you recompute the frequency table every time you shift the window
        #   which isn't great if p is very long.

        from collections import Counter 
        idxs = []  

        freq_p = Counter(p)

        i, j = 0, len(p) - 1
        while j < len(s): 
            if Counter(s[i:j + 1]) == freq_p: 
                idxs.append(i)

            i, j = i + 1, j + 1

        return idxs


if __name__ == '__main__':
    print(Solution().findAnagrams('abab', 'ab'))
