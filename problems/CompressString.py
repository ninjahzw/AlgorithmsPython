"""
Problem:
Interview Questions 
Design a algo. to compress a string. 
If there are multiple repeated characters aaaa, put a3 instead. 
Need to deal with numbers and math equations

Idea:
O(n) solution, no extra space.
"""
class CompressString:
    
    # @input a sting
    # @output compressd string
    def compress(self, src):
        if src is None or len(src) < 2:
            return src
        # current always points to current last index  
        current = -1
        counter = 1
        src = list(src)
        for i in xrange(1, len(src)):
            if src[i] == src[i-1]:
                counter += 1
            else:
                if counter == 1:
                    current += 1
                    src[current] = src[i-1]
                else:
                    src[current+1] = src[i-1]
                    src[current+2] = str(counter)
                    current += 2
                    counter = 1

        if counter == 1:
            current += 1
            src[current] = src[i-1]
        else:
            src[current+1] = src[i-1]
            src[current+2] = str(counter)
            current += 2
            counter = 0
        if current < len(src) - 1:
            return ''.join(src[0:current+1])
        else: 
            return ''.join(src)
print CompressString().compress("aaabccdd") 
print CompressString().compress("a") 
