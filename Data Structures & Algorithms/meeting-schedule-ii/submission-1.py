"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        n=len(intervals)
        st=sorted(interval.start for interval in intervals)
        end=sorted(interval.end for interval in intervals)
        c=0
        j=0
        for s in st:
            if s<end[j]:
                c+=1
            else:
                j+=1
        
        return c
        