class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        """
            2024-05-20

            Issue was correctly defining what new search space is at a branch point
        """

        res = []
        candidates.sort()
        n = len(candidates)
        def search(i, combo, subtotal):
            if subtotal > target:
                return
            elif subtotal == target:
                res.append(combo.copy())
            else:
                for j in range(i, n):
                    if j > i and candidates[j] == candidates[j - 1]:
                        # Skip this A[j + 1:] because would duplicates
                        continue
                    # New search space is A[j + 1:] because decided to include A[j]
                    search(j + 1, combo + [candidates[j]], subtotal + candidates[j])

        search(0, [], 0)
        return res
        """
            2024-05-20

            Some more incorrect algorithms for preventing reusing things
        """


        res = []
        candidates.sort()
        n = len(candidates)
        def search(i, combo, subtotal):
            if subtotal > target:
                return
            elif subtotal == target:
                res.append(combo.copy())
            else:
                # I'm trying to figure out what's going on here.
                for j in range(i + 1, n):
                    if candidates[j] != candidates[j - 1]:
                        # The problem with this is we're reconsidering an element we've already added
                        # The search space here is A[j:] but we included  A[j] in candidate set already! Duplicates!
                        search(j, combo + [candidates[j]], subtotal + candidates[j])



        search(0, [], 0)
        return res

        res = []
        candidates.sort()
        n = len(candidates)
        def search(i, combo, subtotal):
            if subtotal > target:
                return
            elif subtotal == target:
                res.append(combo.copy())
            else:
                for j in range(i, n): # more trying to figure out what's going on here
                    if j != i and candidates[j] != candidates[j - 1]:
                        search(j, combo + [candidates[j]], subtotal + candidates[j])


        search(0, [], 0)
        return res



        """
            2024-05-20
            Unlike with combination sum, sorting here will help with _avoiding_ duplicates

            Each branch point for generating new partial solution looks at  A[j:] for j in range(i, n)
            - But need to skip any A[i+ 1] where A[i+1] == A[i]
        """
        res = []
        candidates.sort() # This is inplace
        n = len(candidates)
        def search(i, combo, subtotal):
            if subtotal > target:
                return
            elif subtotal == target:
                res.append(combo.copy())
            else:
                for j in range(i, n):
                    if j != i and candidates[j] == candidates[j - 1]:
                        continue
                    search(j, combo + candidates[j], subtotal + candidates[j])



        return res

        """
            Alternative solution is instead of thinking of include/exclude element i, we
            are instead greedily starting on subarrays A[1:], A[2:], A[3:] ,....

            I don't really get that solution

            Either way:
            - What we really are doing is a general constraint satisfaction problem.
              we are looking for a subset that satisifes some constraint.

        """

        """
            This gets all the relevant sets
            but can't handle duplicates

        """
        res = []

        def backtrack(curr, start, total):
            if total == target:
                res.append(curr.copy())
            elif total > target:
                return
            else:
                #
                #   The problem is here: how do we prevent using a number twice?
                #
                prev = -1 # Dislike this index fiddling because it's not "wholemeal programming"
                for i in range(start, len(candidates)):
                    if candidates[i] == prev:
                        # Idea:
                        # - If we have 1, 1, ..., 7
                        #   We just don't start the search again at the second 1 to avoid the duplication
                        continue
                    curr.append(candidates[i])
                    backtrack(curr, start + 1, total + candidates[i])
                    curr.pop()
                    prev = i



        candidates.sort()
        backtrack([], 0, 0)
        return res


        """
            Second attempt: Fixed the out of bounds error but it seems to not be exploring
            the space properly...

            It reuses stuff.

            The "cannot reuse duplicates" thing is what makes it hard.

        """


        res = []

        def backtrack(i, s, total):


            if i >= len(candidates):
                return

            elif total == target:
                res.append(s.copy())
                return
            else:
                # Either we current one
                s.append(candidates[i])
                backtrack(i + 1, s, total + candidates[i])
                s.pop()

                # Or we don't
                backtrack(i + 1, s, total)

        backtrack(0, [], 0)
        return res


        """
            First attempt...get an out of bounds error from trying to append ith candidate?

        """

        res = []
     
        def backtrack(i, s, total): 
            if i > len(candidates):
                return 
            
            if total == target: 
                res.append(s.copy())
                return
            
            # Either we current one
            s.append(candidates[i])
            backtrack(i + 1, s, total + candidates[i])
            s.pop()

            # Or we don't
            backtrack(i + 1, s, total)

        backtrack(0, [], 0)
        return res