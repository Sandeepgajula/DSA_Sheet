class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        left,right=0,n-1
        left_max,right_max=0,0
        total=0
        while(left<=right):
            if left_max<right_max:
                left_max=max(left_max,height[left])
                if left==0 or min(left_max,right_max)<height[left] :
                    total+=0
                else:
                    total+= min(left_max,right_max) - height[left] 
                left+=1

            
            else:
                right_max= max(right_max,height[right])
                if right==n-1 or min(left_max,right_max)<height[right]:
                    total+=0
                else:
                    total+= min(left_max,right_max) - height[right] 
                right-=1
        
        return total