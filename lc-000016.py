class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        nums.sort() 

        closest = float('inf')

        n = len(nums)
        for i in range(n - 2):
            j, k = i + 1, n - 1

            while j < k: 
                curr = nums[i] + nums[j] + nums[k]

                # Try to update closest sum
                closest = curr if abs(curr - target) < abs(closest - target) else closest

                # Try to inch pointers to a triplet that sums closer to the target
                if curr > target:
                    k -= 1
                elif curr < target:
                    j += 1 
                else: 
                    break

        return closest
