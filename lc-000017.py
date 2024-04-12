class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

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