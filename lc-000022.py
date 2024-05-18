class Solution:
    def generateParenthesis(self, n: int) -> List[str]:


        """
            Slightly make it faster by having only one variable to track strings
            - but makes code more ugly
        """

        res = []
        s = ''

        def backtrack(l, r):
            nonlocal s
            if l + r == 0:
                res.append(s)
                return

            if l > 0:
                s = s + '('
                backtrack(l - 1, r)
                s = s[:-1]


            if l < r:
                s = s + ')'
                backtrack(l, r - 1)
                s = s[:-1]


        backtrack(n, n)
        return res


        """
            Same logic as below, except we count down
        """
        res = []
        def backtrack(str, left, right):
            if left == right == 0:
                res.append(str)
                return

            else:
                if left > 0: backtrack(str + '(', left - 1, right)
                if left < right: backtrack(str + ')', left, right - 1)


        backtrack('', n, n)
        return res


        """
            Basic working solution.

            Can you imagine the tree for generating these brackets?

        """

        res = []
        def backtrack(s, l, r):

            if len(s) == 2 * n:
                res.append(s)
                return
            else:
                if l < n:
                    backtrack(s + '(', l + 1, r)

                if l > r:
                    backtrack(s + ')', l, r + 1)



        backtrack('', 0, 0)

        return res

        """
            Initial broken solution

            Well, there are going to be C_n number of trees
            Generate all 2n Dyck words

            Trick is: use two variables to keep track of left and right parens
        """
        res = []
        def backtrack(s, l, r): 
            if len(s) == 2 * n: 
                res.append(s)
                return 

            if l > r:
                backtrack(s + '(', l - 1, r) 
            else: 
                backtrack(s + ')', l, r - 1)
            

        backtrack('', n, n)
    
        return res