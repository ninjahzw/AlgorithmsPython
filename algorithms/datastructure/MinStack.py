"""
Problem:
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.

Idea:
Two stacks, the other one keep track of the minimum.
"""

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    # @param x, an integer
    # @return an integer
    def push(self, x):
        self.stack.append(x)
        # NOTE if x={top of min stack} also put x in, so that we can do pop currectly.
        if len(self.min_stack) == 0 or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    # @return nothing
    def pop(self):
        if len(self.stack) > 0:
            if self.stack[-1] == self.min_stack[-1]:
                self.min_stack.pop()
            self.stack.pop()

    # @return an integer
    def top(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        # error message
        return -1

    # @return an integer
    def getMin(self):
        if len(self.min_stack) > 0:
            return self.min_stack[-1]

min_stack = MinStack()
#min_stack.push(-2)
#min_stack.push(0)
#min_stack.push(-1)
#
#print min_stack.top(), min_stack.getMin()
#min_stack.pop()
#print min_stack.top(), min_stack.getMin()

min_stack.push(-1)
print min_stack.top(), min_stack.getMin()

                                                                    
