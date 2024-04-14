class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        """

            Idea:
            - "Process" with increasingly shorter suffix arrays, we only add elements to the _right_ of current element
            - Let the recursion deal with "nesting the appropriate number of loops" (in this case k loops)
            - watch out for off by one errors
        """

        res = []
        def search(start, combo):
            if len(combo) == k: 
                res.append(combo.copy())
                return 

            for i in range(start, n + 1): 
                # Try adding only elements to the _right_ of start - 1
                combo.append(i)
                search(i + 1, combo)
                combo.pop()

        search(1, [])
        return res
        