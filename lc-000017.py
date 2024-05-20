class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        """
            It's not really all that much faster...
        """
        if not digits: return []

        res = []
        chars = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        word = ''

        n = len(digits)

        def backtrack(i):
            nonlocal word
            if i >= n:
                res.append(word)
                return

            for char in chars[int(digits[i])]:
                word += char
                backtrack(i + 1)
                word = word[:-1]

        backtrack(0)

        return res

        """
            Another solution after studying backtracking in more depth
            - We're not operating on a single global variable
            - So we don't need to add/remove from what is essentially a stack

        """
        if not digits: return []

        res = []
        chars = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

        n = len(digits)

        def backtrack(i, word):
            if i >= n:
                res.append(word)
                return

            for char in chars[int(digits[i])]:
                backtrack(i + 1, word + char)

        backtrack(0, '')

        return res


        """
            Improved version that only does string operations
            but the intuition of how we're building the strings is the same
        """
        res = []
        if not digits: return res


        n = len(digits)
        chars = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

        def search(i, string):
            if i >= n:
                res.append(string)
                return

            # Decision making: for the next digit, either add or
            # don't add a char and then go to the letter string of the next digit
            for char in chars[int(digits[i])]:
                string += char
                search(i + 1, string)
                string = string[:-1]

        search(0, '')
        return res



        #
        #   Trying an even more compact solution
        #   - Not really any advantage
        #
        res = []
        if not digits: return res

        chars = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

        n = len(digits)
        stack = []

        def backtrack(i):
            if i == n : res.append(''.join(stack)); return

            for c in chars[int(digits[i])]:
                stack.append(c)
                backtrack(i + 1)
                stack.pop()


        return res

        #
        #  Save some space with a stack
        #  - Basically backtracking is using a dfs
        #
        res = []
        if not digits: return res
        mapping = {
            '1': '', '2': 'abc', '3': 'def', '4':'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz', '0': ''
        }
        n = len(digits)

        stack = []
        def backtrack(i):
            if i == n:
                # Reached a leaf
                res.append(''.join(stack))
                return

            for c in mapping[digits[i]]:
                stack.append(c)
                backtrack(i + 1)
                stack.pop()

        backtrack(0)
        return res


        #
        #  Generic solution
        #  - Depends on fact recursion stops when string we're making is
        #    same as length of digits
        #   Time: O(n4^n)
        #

        res = []    
        if not digits:
            return 

        mapping = {
            '1': '', '2': 'abc', '3': 'def', '4':'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz', '0': ''
        }
        
        n = len(digits)

        def backtrack(i, curr): 
            if len(curr) == n: 
                res.append(curr)
                return
            for c in mapping[digits[i]]: 
                backtrack(i + 1, curr + c)
        backtrack(0, '')
        return re