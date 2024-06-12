class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        """
            It's not "remove duplicates", it's don't add them in the first place

            I'm not 100% sure I understand this algorithm, especially the part about the last occurrence stuff
        """
        
        last_occurrence = { char:i for i, char in enumerate(s) }
        
        monotonic_stack = []
        
        # Inuition: try single pass greedy
        for i, char in enumerate(s): 

            if char not in monotonic_stack:
                # ... skipping all duplicates

                # Keep deleting characters until current element is the "highest"
                # e.g. if stack is "bc" but we see an "a" then throw out everything
                #      and restart the stack
                stack_top = monotonic_stack[-1]
                while (
                    monotonic_stack and             # Greedy keep deleting if we see a "better" one
                    char < stack_top and 
                    i < last_occurrence[stack_top]  # ????
                ): 
                    monotonic_stack.pop()

                # Then append it 
                monotonic_stack.append(char)
        return "".join(monotonic_stack)
        
        """
            IDEAS: 

            Greedy in the sense of: throw out elements in the stack if we see something smaller
            
            Rather than remove duplicates, just simply don't ADD repeated elements?
            - See, I thought about deleting letters in the string (again back to the idea that for any array problem, probably useful to consider if you can find
              a one pass solution )
            
            Two ways of looking at this: 
            - deleting chars from s to get result 
            - iteratively taking one character at a time

            How do we guarantee "lexicographically smallest?"
            
            => Monotonic stack to keep results (greedily look)

        """

        pass
