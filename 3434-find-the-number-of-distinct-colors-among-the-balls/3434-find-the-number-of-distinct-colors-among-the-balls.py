class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ballColors = defaultdict(int)
        colorFreq = defaultdict(int)

        res = []

        for (ball , newColor) in queries:
            if ball not in ballColors:
                ballColors[ball] = newColor
                colorFreq[newColor] += 1
            else:
                prevColor = ballColors[ball]
                if colorFreq[prevColor] == 1:
                    del colorFreq[prevColor]
                else:
                    colorFreq[prevColor] -= 1
                ballColors[ball] = newColor
                colorFreq[newColor] += 1
            
            res.append(len(colorFreq))

        return res
        