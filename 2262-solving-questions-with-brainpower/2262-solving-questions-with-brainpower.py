class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = {}
        def dfs(i):
            if i >= len(questions):
                return 0
            if i in dp:
                return dp[i]
            points , brainpower = questions[i]
            dp[i] = max(points + dfs(i + brainpower + 1) , dfs(i+1))
            return dp[i]


        return dfs(0)               