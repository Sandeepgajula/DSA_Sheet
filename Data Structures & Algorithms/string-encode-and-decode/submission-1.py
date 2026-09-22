class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            j = i
            # Find where the length ends and delimiter starts
            while s[j] != '#':
                j += 1
            
            length = int(s[i:j])
            i = j + 1  # Move past the '#'
            
            # Extract the exact substring using the length
            res.append(s[i : i + length])
            i += length  # Move pointer to the start of the next item
            
        return res