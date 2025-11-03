class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        result = 0
        i = 0 

        while i < len(colors) - 1:
            j = i + 1
            if colors[i] != colors[j]:
                i += 1
                continue
            
            max_time= neededTime[i]
            total_sum = neededTime[i]

            while j < len(colors) and colors[i] == colors[j]:
                total_sum += neededTime[j]
                max_time = max(max_time,neededTime[j])
                j += 1

            result += total_sum - max_time
            i = j

        return result        