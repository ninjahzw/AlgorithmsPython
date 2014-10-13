"""
Problem:
10 most common word in a text file

Solution:
create Word object and compare on count variable.
NOTE: this solution including:
Python Buffered I/O operation
Python override "toString" (__repr__) and "compareTo" (__lt__) like in Java
"""

import io
import heapq

class Word:
    def __init__(self,word,count):
        self.word = word
        self.count = count

    def __lt__(self, other):
        return self.count < other.count

    def __repr__(self):
        return 'word: ' + self.word + ' count: ' + str(self.count)

class TopTen:
    def __init__(self):
        return

    def top_ten(self):
        lines = None
        dic = dict()
        with io.open('/Users/houzhaowei/files','r') as file:
            # buffered read file.
            # lines = file.readlines() is not buffered read.
            for line in file:
                line = str(line.replace('\n',''))
                if line in dic:
                    dic[line] = dic[line] + 1
                else:
                    dic[line] = 1
        result = []
        for one in dic:
            word = Word(one,dic[one])
            heapq.heappush(result,word)
            # because we only want top 10,so pop the smallest out if
            # length is greater than 10.
            if (len(result)) >= 10:
                heapq.heappop(result)

        while result:
            print heapq.heappop(result)
########
TopTen().top_ten()