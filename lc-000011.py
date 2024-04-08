class Solution:
    def maxArea(self, height: List[int]) -> int:

        #
        #  This is a greedy algorithm
        #   - basically kick along whichever pointer i or j points to the lower height to see if we can get a better height
        #   - since dx = 1 every time, but we could get improvements to dh more than 1 if we kick the pointer along
        #

        i, j = 0, len(height) - 1 

        area = min(height[i], height[j]) * (j - i)

        while i <= j: 

            h = min(height[i], height[j])
            area = max(area, h * (j - i))

            if height[i] < height[j]: 
                i += 1
            else: 
                j -= 1

        return area