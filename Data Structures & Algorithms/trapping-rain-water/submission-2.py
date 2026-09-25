class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        left,right=0,n-1
        left_max,right_max=0,0
        total=0
        while(left<=right):
            if left_max<right_max:

                if  height[left] > left_max:
                    left_max=max(left_max,height[left])
                else:
                    total+= left_max - height[left]
                left+=1

            
            else:
                right_max= max(right_max,height[right])
                if  height[right] > right_max:
                    right_max=max(right_max,height[left])
                else:
                    total+= right_max - height[right]

                right-=1
        
        return total