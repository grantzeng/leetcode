class Solution:
    def uniqueLetterString(self, s: str) -> int:


        #
        #   Reattempt at bruteforce recursive search on all substrings
        #    - Issue with initial attempt was it was discarding substrings that
        #      had same sequence but were in different positions
        from collections import Counter
        seen = set()
        count = 0

        def recurse(i, j, size, s, seen):
            nonlocal count
            # Assume we index strings with last element exclusive
            ss = s[i:j]
            idx = (i, j)

            if idx in seen or not ss:
                # Substring has already been processed or is empty
                return 0
            print(ss)

            # Add current value to count
            count += sum(c for c in Counter(ss).values() if c == 1)

            for i in range(i, j - size + 1):
                count += recurse(i, i + size, size - 1, s, seen)

            return count

        n = len(s)
        count = recurse(0, n, n, s, seen)
        return count



        # return count

        #
        #   Try bruteforce iterative solution checking all C(n + 1,2) substrings (it's n + 1 because
        #   string slicing is not inclusive of end!)
        #
        #   Time: O(n^3) since it's O(C(n + 1, 2) * O(n)) - counting costs O(n) for each substring
        #   Space: O(1)
        # from collections import Counter
        # n = len(s)
        # count = 0
        # for i in range(n):
        #     for j in range(i, n):
        #         substring = s[i: j + 1]
        #         print(substring)
        #         #count += sum(count for count in Counter(substring).values() if count == 1)

        # return count


        #
        #
        #   Initial attempt: recursion with memoisation (INCORRECT SOLUTION)
        #
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


        #
        #   Process journal:
        #   - Initially counted number distinct characters (wrong!) 103 on LEETCODE
        #   - but really we wanted characters with no repetition!: 90 on 'LEETCODE'
        #
        #   The problem here is you didn't really get what the problem was was asking for
        #
        from collections import Counter
        memo = {}
        def recurse(substring, k):

            if not substring:
                # Explored this branch already
                return
            print(substring)
            memo[substring] = sum(count for count in Counter(substring).values() if count == 1)
            # Recurse on sliding window of size k - 1
            n = len(substring)
            for i in range(n - (k - 1) + 1):
                recurse(substring[i:i + k - 1], k - 1)

        recurse(s, len(s))

        # print(memo)

        return sum(memo.values())


if __name__ == '__main__':
    #assert(Solution().uniqueLetterString('ABC') == 10)
    #assert(Solution().uniqueLetterString('ABA') == 8)
    print(Solution().uniqueLetterString('LEETCODE'))