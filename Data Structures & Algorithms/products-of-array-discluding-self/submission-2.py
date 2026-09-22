class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        c = 0
        for num in nums:
            if num==0 :
                c+=1
            else:
                prod*=num
        
        if c>1:
            return [0]*len(nums)

        res=[0]*len(nums)
        for i,j in enumerate(nums):
            if c:
                res[i] = 0 if j else prod
            else:
                res[i]=prod//j
                
        return res

        