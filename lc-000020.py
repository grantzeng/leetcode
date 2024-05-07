class Solution:
    def isValid(self, s: str) -> bool:

        """
            Working solution:
            - Don't pop from an empty stack, basically
            - If there's elements left in the stack, means we had unmatched bracket
        """

        stack = []
        match = { ')': '(', '}': '{', ']': '[' }

        for token in list(s): 
            if token in ['(', '{', '[']: 
                stack.append(token)
            else:
                if not stack or match[token] != stack.pop(): 
                    return False

        return not stack