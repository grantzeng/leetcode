class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        """
            2024-05-20
            Fixed solution where we sort input array first.
            - The search should've been restarted at A[j:] after we add A[j] to the array
              not at the current suffix array of A[i:] !!!
            - That's how we got non monotonic outputs like [2, 3, 2]!

            Still not really apparent to me what benefit is here of the presorting
            other than "here's something that works".
        """
        res = []
        candidates.sort()
        n = len(candidates)

        def search(i, combo, subtotal):
            if subtotal > target or i >= n:
                return
            elif subtotal == target:
                res.append(combo.copy())
            else:
                for j in range(i, n):
                    # Alternative to push/pop candidate[j], which is effectively
                    # what backtracking is doing, we just make the actual partial solution instead
                    search(j, combo + [candidates[j]], subtotal + candidates[j])


        search(0, [], 0)
        return res
        """
            2024-05-20
            Rewriting the alternative solution where we sort the input first

            I'm not sure why this algorithm is incrorect....
            https://leetcode.com/problems/combination-sum-ii/solutions/750378/python3-dfs-solutions-templates-to-6-different-classic-backtracking-problems-more
            - If you see here the code looks basically the same?

            What I'm confused about is why this code generates non-monotonic sequences?

            E.g. [[2,2,3],[2,3,2],[3,2,2],[7]]
            - The first one is fine, but how did [2, 3, 2] turn up?

        """
        res = []
        candidates.sort()
        n = len(candidates)

        def search(i, combo, subtotal):
            if subtotal > target or i >= n:
                return
            elif subtotal == target:
                res.append(combo.copy())
            else:
                for j in range(i, n): # I think the  problem is here.
                    # If i is at 2, but we add element at 3,  well we might end up adding elements before j
                    search(i, combo + [candidates[j]], subtotal + candidates[j])


        search(0, [], 0)
        return res

        """
            2024-05-02
            Rewriting of the solution where we either:
            - Include ith number (this what allows repeats)
            - Or continue search at i + 1th number and exclude adding ith again

            Reminder that we're doing a depth first search of the partial candidate tree
        """
        res = []
        n = len(candidates)
        def search(i, combo, subtotal):
            if subtotal > target or i >= n:
                return

            elif subtotal == target:
                res.append(combo.copy())

            else:
                # This doesn't work because combo.append() returns a None object
                # search(i, combo.append(candidates[i]), subtotal + candidates[i])

                # You have to have something that returns a list (which is what + will do)
                search(i, combo + [candidates[i]], subtotal + candidates[i])
                search(i + 1, combo, subtotal)

        search(0, [], 0)

        return res



        """
            An alternative solution I was reading about which _sorts_ everything first

            It's not entirely obvious to me what the corresponding tree implicitly is.
            - In my original solution it's simply add/don't add ith element for the decision making.

            For this one...? Not so sure.
        """
        if not candidates:
            return []

        res = []

        candidates.sort()
        def backtrack(idx, path, curr):
            if curr > target:
                return
            elif curr == target:
                res.append(path.copy())
            else:
                for i in range(idx, len(candidates)):
                    backtrack(i, path + [candidates[i]], curr + candidates[i])

        backtrack(0, [], 0)
        return res



        """
            Slightly quicker version that tracks combo in a variable rather than by pass
            - Combo is basically a stack and we make a copy of stack state when it sums to total
        """

        res = []

        combo = []
        def search(i, total):
            if total == target:
                res.append(combo.copy())
                return

            if i >= len(candidates) or total > target:
                return

            # Try including candidate i
            # - This lets us do repetitions e.g. search(i, *) will call search(i, *) and search(i + 1, *)
            combo.append(candidates[i])
            search(i, total + candidates[i])

            # Try excluding candidate i
            combo.pop()
            search(i + 1, total)

        search(0, 0)
        return res

        """
            Working solution

        """
        res = []

        def search(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return

            if i >= len(candidates) or total > target:
                return

            # Either we add candidate i
            curr.append(candidates[i])
            search(i, curr, total + candidates[i])

            # Or we don't add candidate i
            curr.pop()
            search(i + 1, curr, total)
        
        search(0, [], 0)
        return res



        """

            Initial broken solution

        """
        res = []
 
        stack = []
        n = len(candidates)
        def search(i): 
            if i > n: return 
            
            if sum(stack) == target: 
                res.append(stack.copy())
                return
            elif sum(stack) > target: 
                return

            stack.append(candidates[i])
            search(i + 1)
            stack.pop()   

        search(0)
        return res