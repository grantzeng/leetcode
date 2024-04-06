class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        #
        #   Two pointer solution that does work
        #   - Have a helper function to grab next token
        #   - Traverse the strings backward to AVOID having to backtrack
        #     (generally try to do things in single passes for arrays)
        #

        # This will grab the next valid token
        def next_valid_char(str, idx):
            backspace = 0
            while idx >= 0:
                if backspace == 0 and str[idx] != '#':
                    break
                elif s[idx] == '#':
                    # Preceding char needsto be deleted
                    backspace += 1
                else:
                    # A char that was deleted
                    backspace -= 1
                idx -= 1
            char = str[idx] if idx >= 0 else ""
            return (idx, char)

        # This traverses s and t in reverse to avoid having to backtrack
        # or keep track of backspaced characters
        idx_s, idx_t = len(s) - 1, len(t) - 1
        while idx_s >= 0 or idx_t >= 0:
            idx_s, char_s = next_valid_char(s, idx_s)
            idx_t, char_t = next_valid_char(t, idx_t)

            if char_s != char_t:
                return False

            idx_s -= 1
            idx_t -= 1

        return True


        #
        #   Two pointer solution
        #   - The issue with parsing from left to right is having to backtrack
        #     so you might think: how do I do this without backtracking
        #
        #   THIS IS BROKEN: but almost works.
        #

        def next_valid_char(s, idx):
            backspace = 0
            while idx >= 0:
                if backspace == 0 and s[idx] != '#':
                    break
                elif s[idx] == '#':
                    # Preceding char needsto be deleted
                    backspace += 1
                else:
                    # A char that was deleted
                    backspace -= 1
                idx -= 1
            return idx

        # The problem here is how do we maintain invariant that indexes are valid
        idx_s, idx_t = len(s) - 1, len(t) - 1
        while idx_s >= 0 and idx_t >= 0:
            idx_s = next_valid_char(s, idx_s)
            idx_t = next_valid_char(t, idx_t)

            if s[idx_s] != t[idx_t]:
                return False

            idx_s -= 1
            idx_t -= 1

        return True

        #
        #   Initial stack based solution
        #   - Basically, check resource is available before trying to do something
        #     (don't pop from an empty stack)
        #   - Does the obvious parse left to right
        #
        #   Time: O(|s| + |t|)
        #   Space : O(|s| + |t|)
        #
        s_stack, t_stack = [], []

        for c in s: 
            if c != '#': 
                s_stack.append(c)
            else:
                if s_stack: s_stack.pop()

        for c in t: 
            if c != '#': 
                t_stack.append(c)
            else: 
                if t_stack: t_stack.pop()

        while s_stack and t_stack: 
            if s_stack.pop() != t_stack.pop(): 
                return False
        
        return not (s_stack or t_stack)

        