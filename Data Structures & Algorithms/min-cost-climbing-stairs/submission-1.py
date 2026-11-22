class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        res=[-1] * (n+1)
        def mincost(res,i):
            if i>=n:
                return 0
            if res[i]!=-1:
                return res[i]
            res[i]=cost[i]+min(mincost(res,i+1),mincost(res,i+2))
            return res[i]
        
        return min(mincost(res,0),mincost(res,1))
        