class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        mx,c=0,1
        if len(nums)<=1:
            return len(nums)
        for i in range(len(nums)-1):
            if (nums[i+1]-nums[i])==1:
                c+=1
            elif nums[i] == nums[i+1]:
                pass
            else:
                c=1

            mx=max(c,mx)
        
        return mx
        