class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        prevStrat , prevEnd = meetings[0]
        res = prevStrat - 1
        for i in range(1,len(meetings)):
            start , end = meetings[i]
            if start > prevEnd :
                res += start - prevEnd - 1
                prevEnd = end
            prevEnd = max(prevEnd , end)

        res += days - prevEnd

        return res
        