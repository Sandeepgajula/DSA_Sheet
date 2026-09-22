class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp={}
        for st in strs:
            w="".join(sorted(st))
            if w in mp:
                mp[w].append(st)
            else:
                mp[w]=[st]
        
        return list(mp.values())
            

        