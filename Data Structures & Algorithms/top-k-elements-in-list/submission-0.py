class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp={}
        for num in nums:
            mp[num]=mp.get(num,0)+1
        
        res = sorted(mp.keys(),key=lambda key:mp[key],reverse=True)
        
        return res[:k]
        