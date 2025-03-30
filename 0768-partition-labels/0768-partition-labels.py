class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        mp = {}

        for i , ch in enumerate(s) :
            if ch in mp :
                mp[ch][1] = i
            else:
                mp[ch] = [i,i]

        values = list(mp.values()) 
        res = []
        i =  0
        while i < len(values):
            start , end = values[i]
            j = i + 1
            while j < len(values) and end > values[j][0] :
                end = max(end,values[j][1])
                j += 1
            res.append(end - start + 1)
            i = j 

        return res
