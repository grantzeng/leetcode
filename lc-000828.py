class Solution:
    def uniqueLetterString(self, s: str) -> int:

        #
        #
        #   Initial attempt: recursion with memoisation
        #   - This solution is broken because it's not counting unique characters properly
        #   - Also you didn't read the instructions which asked you to write a separate function...
        #
        #   Time: O(C(|s|, 2) * O(|s|)) which is O(|s|^3) or cubic worst case brute forcing
        #         every substring (since have to examine every substring for number of unique
        #         chararacters)
        #
        #   Space: O(|s|^2) since we record every substring.
        #
        #   If a string is length n, then there's C(n, 2) = n(n - 1)/2 = O(n^2) substrings
        #
        memo = {}
        def recurse(substring, k):
            if substring in memo or not substring:
                # Explored this branch already
                return
            print(substring)
            memo[substring] = len(set(substring))

            # Recurse on sliding window of size k - 1
            n = len(substring)
            for i in range(n - (k - 1) + 1):
                recurse(substring[i:i + k - 1], k - 1)

        recurse(s, len(s))

        print(memo)

        return sum(memo.values())


if __name__ == '__main__':
    #assert(Solution().uniqueLetterString('ABC') == 10)
    #assert(Solution().uniqueLetterString('ABA') == 8)
    print(Solution().uniqueLetterString('LEETCODE'))