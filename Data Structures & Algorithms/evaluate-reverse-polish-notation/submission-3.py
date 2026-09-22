class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack =[]
        for token in tokens:
            if token in ["+","-","*","/"]:
                if len(stack)<2:
                    return -1
                val1=stack.pop()
                val2=stack.pop()
                val=0
                if token== "+":
                    val=val2+val1
                elif token =="-":
                    val = val2-val1
                elif token == "*":
                    val = val2 * val1
                else:
                    val = int(val2/val1)
                stack.append(val)
            
            else :
                stack.append(int(token))
        
        return stack[-1]
        