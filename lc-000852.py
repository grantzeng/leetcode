class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:

        """
            This is exactly the same peak finding algorithm as 162
        """
        n = len(arr)
        i, j = 0, n - 1
        while i <= j:
            mid = i + (j - i) // 2
            if mid > 0 and arr[mid] < arr[mid - 1]:
                j = mid - 1
            elif mid < n - 1 and arr[mid] < arr[mid + 1]:
                i = mid + 1
            else:
                return mid
