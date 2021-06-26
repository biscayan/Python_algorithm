class Solution:
    def isValid(self, s: str) -> bool:
    
        stack = []

        for p in s:
            if p == '(' or p == '[' or p == '{':
                stack.append(p)
            else:
                if not stack:
                    return False
                else:
                    if p ==')':
                        if stack[-1] == '(':
                            stack.pop()
                        else:
                            return False
                    elif p ==']':
                        if stack[-1] == '[':
                            stack.pop()
                        else:
                            return False
                    elif p =='}':
                        if stack[-1] == '{':
                            stack.pop()
                        else:
                            return False
                            
        if stack:
            return False
        else:
            return True