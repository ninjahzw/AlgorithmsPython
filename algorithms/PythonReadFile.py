# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution:

    def __init__(self):
        self.filename = 'test'

    # @param buf, Destination buffer (a list of characters)
    # @param n,   Maximum number of characters to read (an integer)
    # @return     The number of characters read (an integer)
    def read(self, buf, n):
        int result = 0
        while self.read4(buf) == 4:
            result += 4

    def read4(buf):
        with open(self.filename, 'r+') as f:
            for line in f:
                
