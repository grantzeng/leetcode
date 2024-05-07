class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:



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