class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        """
            Working solution
            - The issue is the 'off by one error', upper bound of range is exclusive
            - Basically idea is to look at A[idx + 1:] as the rest of the search space
              since we included A[idx] already.

            - A in this case is implicit, since we just use range function


        """
        res = []

        def search(idx, combo, subtotal):
            if len(combo) > k or subtotal > n:
                return
            elif len(combo) == k and subtotal == n:
                res.append(combo.copy())
            else:
                for j in range(idx + 1, 10):
                    search(j, combo + [j], subtotal + j)

        search(0, [], 0)
        return res


        """

            2024-05-21
            Almost working solution
            - Need to think a bit more clearly about the search space
            - I don't really like the if statement (and it's not necessary)
        """
        res = []
        def search(idx, combo, subtotal):
            if len(combo) > k or subtotal > n:
                return
            elif len(combo) == k and subtotal == n:
                res.append(combo.copy())
            else:
                for j in range(max(1, idx), 9):
                    if j in combo: continue
                    search(j + 1, combo + [j], subtotal + j)

        search(0, [], 0)
        return res



        """
            2024-05-21
            Initial broken solution
            - Not sure if should just explicitly allocate an array at the
              start to make the logic easier for me.
        
        """

        res = []

        def search(combo, subtotal): 
            if len(combo) > k or subtotal > n: 
                return 
            elif subtotal == n: 
                res.append(combo.copy())
            else: 
                for i in range(max(combo) if combo else 1, 10): 
                    search(combo + [i], subtotal + i)
        search([], 0)
        return res