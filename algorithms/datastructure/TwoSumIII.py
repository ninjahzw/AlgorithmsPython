"""
Problem:
Design and implement a TwoSum class. It should support the following operations: add and find.

add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value.

For example,
add(1); add(3); add(5);
find(4) -> true
find(7) -> false

Idea:
NOTE: 
This is slightly different to TwoSum, 
because TwoSum builds up the hashmap then traversing the array, no need to worry about duplicate values,
this time, however, the hashmap is built up by add function, when execute find function,
can directly use the already set up hashmap.
However, in this condition, duplicate value may exists, so a counter and further check is needed.
"""
class TwoSum:

    # initialize your data structure here
    def __init__(self):
        self.table = dict()            

    # @return nothing
    def add(self, number):
        # since can't know the index, must store a counter.
        # can use this counter to prevent duplicate value.
        # NOTE the usage of dict.get(number, 0) is when no such key then return 0.
        self.table[number] = self.table.get(number, 0) + 1
                                

    # @param value, an integer
    # @return a Boolean
    def find(self, value):
        for x in self.table:
            y = value - x
            # NOTE if same value, then make sure at least two such value exists.
            # And because we can not go progressively like two sum, we have to do this way
            if (y == x and self.table.get(y, 0) > 1) or (y != x and self.table.get(y, 0) > 0):
                return True
        return False
