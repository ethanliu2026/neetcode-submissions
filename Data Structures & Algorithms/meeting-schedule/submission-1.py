"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) < 2:
            return True
        L = []
        for interval in intervals:
            L.append((interval.start, interval.end))
        L = sorted(L)
        L = [x for t in L for x in t]
        for i in range(len(L)-1):
            if L[i] > L[i+1]:
                return False
        return True
        