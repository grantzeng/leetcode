class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        """
            Second attempt: Fixed the out of bounds error but it seems to not be exploring
            the space properly...

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