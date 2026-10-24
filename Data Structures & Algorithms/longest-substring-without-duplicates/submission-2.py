class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp={}
        l=0
        max_len=0
        for r in range(len(s)):
            c=s[r]
            if c in mp:
                l=max(mp[c]+1,l)
            
            mp[c]=r

            
            max_len=max(max_len,r-l+1)
        

        return max_len
        