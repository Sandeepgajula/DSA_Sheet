import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def feasable(x):
            sum=0
            for pile in piles:
                sum+=math.ceil(pile/x)
            return sum<=h


        left=1
        right=max(piles)
        while(left<right):
            mid=left+(right-left)//2
            if feasable(mid):
                right=mid
            else:
                left=mid+1
        return right

            
        