class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        a=[-1]*n
        def rob(i:int):
            if i>=n:
                return 0
            
            if a[i]!=-1:
                return a[i]
                
            a[i]=nums[i]+max(rob(i+2),rob(i+3))
            return a[i]
        
        return max(rob(0),rob(1))

        