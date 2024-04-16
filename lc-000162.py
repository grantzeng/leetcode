class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        """
            I think this windowing idea works, but need to find a way of keeping m - 1 and m + 1
            as valid indicies

        """


        """
            Another attempt

            If we do the naive algorithm: discrete local maxima finder
            - Obvious O(n) solution is just having a window of size 3 and filtering.
            Trying another algorithm:


            Idea is we check the window around mid.
            but this only deals with okay case where:
                mid is in the middle of a long input and we can have a window
                of size 3.

            - Will break if peak is at 0 or n - 1
            - or if input size < 3
        """
        i, j = 0, len(nums) - 1

        while i < j:
            mid = (i + j) // 2

            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid] > nums[i]:
                i = mid + 1
            else:
                j = mid - 1


        """
            Initial broken solution

            - This fails because on [1, 2, 3, 1]
                mid = 1 initially, but obviously 1 < 2 and 1 < 2 for i and j


        """
        i, j = 0, len(nums) - 1

        while i < j: 
            mid = (i + j) // 2
            if nums[mid] > nums[i] and nums[mid] > nums[j]:
                return mid
            elif nums[mid] > nums[i]: 
                i = mid + 1
            else: 
                j = mid - 1






        