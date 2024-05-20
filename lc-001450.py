class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        """
            Nonsensical one liner written for my own amusement
        """
        return sum([ 1 for start, end in zip(startTime, endTime) if queryTime >= start and queryTime <= end])