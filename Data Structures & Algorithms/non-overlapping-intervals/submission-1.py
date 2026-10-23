class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        c=0
        prevend=intervals[0][1]
        for st,end in intervals[1:]:
            if st >= prevend:
                prevend=end
            else:
                c+=1
                prevend=min(prevend,end)
        
        return c

        