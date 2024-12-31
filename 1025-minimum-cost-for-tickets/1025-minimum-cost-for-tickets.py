class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = {len(days) : 0}
        def backtrack(i):
            if i in dp:
                return dp[i]
            dp[i] = float("inf")
            j = i 
            for cost , duration in zip(costs , [1,7,30]):
                while j < len(days) and days[j] < days[i] + duration :
                    j += 1
                dp[i] = min(dp[i] , cost + backtrack(j))
            return dp[i]

        return backtrack(0)