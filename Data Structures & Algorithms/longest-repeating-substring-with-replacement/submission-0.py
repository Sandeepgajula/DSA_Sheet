class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mp={}
        max_freq,max_len=0,0
        l=0
        for r in range(len(s)):
            c=s[r]
            mp[c]=mp.get(c,0)+1
            max_freq=max(max_freq,mp[c])

            if r-l+1 - max_freq > k:
                mp[s[l]]-=1
                l+=1

            max_len=max(max_len,r-l+1)
        
        return max_len



        