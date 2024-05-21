class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        # 
        #  Naive solution is doing subset 1 algorithm but adding in a check for whether set is already in res
        #  - but need to think of a better solution where we don't traverse duplicates at all
        #

        res = []
        def search(idx, subset): 
            if idx >= len(nums): 
                if subset.copy() not in res:
                    res.append(subset.copy()) 
                return
            
            search(idx + 1, subset + [nums[idx]])
            search(idx + 1, subset)
        
        nums.sort()
        search(0, [])
        return res
        