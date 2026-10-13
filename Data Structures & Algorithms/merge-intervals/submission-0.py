class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda a:a[0])
        ans=[intervals[0]]
        for st,end in intervals:
            lastend=ans[-1][1]
            if lastend>=st:
                ans[-1][1]=max(lastend,end)
            else:
                ans.append([st,end])

        return ans