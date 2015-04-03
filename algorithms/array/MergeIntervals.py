"""
Problem:
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
"""
# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        result = []
        if not intervals or len(intervals) < 1:
            return result
        s = sorted(intervals, key=lambda x:x.start)
        pre = s[0]
        for i in xrange(1, len(s)):
            cur = s[i]
            print pre, cur
            if pre.end >= cur.start:
                pre = Interval(pre.start, max(pre.end, cur.end))
            else:
                result.append(pre)
                pre = cur
        result.append(pre)
        return result

Solution().merge([Interval(1,4), Interval(0,2),Interval(3,5)])
