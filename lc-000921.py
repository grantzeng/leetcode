class Solution:
    def minAddToMakeValid(self, s: str) -> int:

        """
            2024-06-03
            This is a parsing problem.

            - Basically figure out how many right and left parens to insert to complete the tree

            Really we don't need an actual stack, I could optimise this with just having a counter
            but conceptually we need a stack, because this problem is quite similar to #20

        """

        stack = []
        count = 0 
        for token in s: 
            if token == '(': 
                stack.append(token)
            elif token == ')': 
                if stack: 
                    stack.pop()
                else: 
                    # Found an unmatched right paren
                    count += 1
                    
        # Anything remaining on the stack is gonna be an unmatched left paren
        return count + len(stack)