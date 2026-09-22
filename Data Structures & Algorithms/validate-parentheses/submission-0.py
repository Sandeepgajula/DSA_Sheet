class Solution:
    def isValid(self, s: str) -> bool:
        a=[]
        for c in s:
            if c in ['[','{','(']:
                a.append(c)
            elif c in ['}',']',')']:
                if not a:
                    return False
                if c=='}' and a[-1]=='{':
                    a.pop()
                elif c==']' and a[-1]=='[':
                    a.pop()
                elif c==')' and a[-1]=='(':
                    a.pop()
                else:
                    return False
        return True if len(a)==0 else False