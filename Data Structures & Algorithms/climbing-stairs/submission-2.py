class Solution:
    def climbStairs(self, n: int) -> int:

        def climb(n,a):
            if n==1 or n==0:
                return 1
            if a[n]!=-1:
                return a[n]
            
            a[n]=climb(n-1,a) + climb(n-2,a)
            return a[n]
        
        a=[-1]*(n+1)
        return climb(n,a)


        