class Solution:
    def search(self, nums: List[int], target: int) -> int:

        """
            This one also works:
            - Idea is :
                - either i to mid is monotonic (or symmetrically, mid to j)
                  or it isn't
                - then you do the normal binary search thing of trying to kick
                  the bounds i and j towards where target index would be
                  if target exists

        """

        i, j = 0, len(nums) - 1
        while i <= j:
            mid = i + (j - i) // 2

            if nums[mid] == target: return mid

            if nums[i] <= nums[mid]:
                if nums[i] <= target < nums[mid]:
                    j = mid - 1
                else:
                    i = mid + 1
            else:
                if nums[mid] < target <= nums[j]:
                    i = mid + 1
                else:
                    j = mid - 1

        return -1

        """
            Intuition:
            - Do we do a normal binary search or do we not?
            - Have to keep kicking i and j towards index of target (if it exists)
        """
        i, j = 0, len(nums) - 1
        while i <= j: 
            m = i + (j - i) // 2

            if nums[m] == target: 
                return m

            if nums[m] < nums[j]:
                if nums[m] < target <= nums[j]: 
                    i = m + 1
                else: 
                    j = m - 1 
            else: 
                if nums[i] <= target < nums[m]: 
                    j = m - 1
                else: 
                    i = m + 1
        
        return -1