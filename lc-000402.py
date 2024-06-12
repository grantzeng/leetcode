class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        """
            Brute force: 

            There are C(n, k) ways to remove k numbers from num. 
            So brute force is O(n^k) or polynomial time

        """