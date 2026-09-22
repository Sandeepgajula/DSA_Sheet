class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val = 999999999999
        max_prof = -1
        for i in range(len(prices)):
            min_val = min(min_val,prices[i])

            max_prof = max(max_prof,prices[i]-min_val)


        return max_prof