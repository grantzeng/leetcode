class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        subsets = []

        # Variable for creating a subset
        curr = []
        def dfs(level):
            if level >= n:
                # We've made decisions to include/exclude every element
                # - so here is a possible subset, add to "scribble pad"
                subsets.append(curr.copy())
                return
            
            # This encodes the bifurcating along the tree for generating subsets
            # and is where backtracking is happening
            curr.append(nums[level])
            dfs(level + 1)

            curr.pop() 
            dfs(level + 1)
            
        dfs(0)
        return subsets