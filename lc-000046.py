class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        """

            First attempt broken solution (why is it broken?)

        """
        res = []
        n = len(nums)
        nums = set(nums)
        def search(permutation, remaining): 
            if not remaining: 
                res.append(permutation)
                return 
                
            for i, num in enumerate(remaining): 
                permutation.append(num)
                search(permutation, remaining - set([num]))
                permutation.pop()
                search(permutation, remaining) 
        search([], nums)
        return res