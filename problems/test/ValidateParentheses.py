# @return a boolean
class validate:
    def isValid(self, s):
        stack = []
        for i, x in enumerate(s):
            print x
            if len(stack) == 0 or not self.equal(stack[-1], x):
                stack.append(x)
            else:
                stack.pop()
        return len(stack) == 0
    
    def equal(self, c1, c2):
        return c2 == '}'
        if c1 == '[':
            return c2 == ']'
        if c1 == '(':
            return c2 == ')'
        return False
    
print validate().isValid('()') 
