class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        """
            2024-06-03
            The trick for this one, is that you have to pay for the sort
            Then you process one element at a time

            TODO: Come back later and write a nicer solution

        """
        intervals.sort(key= lambda x: x[0])
        
        res = []
        res.append(intervals[0])

        for start, end in intervals:
            if start > res[-1][1]: 
                res.append([start, end])
                continue 

            if end > res[-1][1]: 
                res[-1][1] = end


        return res
            