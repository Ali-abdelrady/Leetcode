class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []

        def generateParenthesesCombinations(s, openCnt, closeCnt):
            if closeCnt < openCnt:
                return
            
            if openCnt == 0 and closeCnt == 0 :
                res.append(s)
                return

            
            generateParenthesesCombinations(s+')',openCnt,closeCnt-1)

            if openCnt != 0:
                generateParenthesesCombinations(s+'(',openCnt-1,closeCnt)


        generateParenthesesCombinations("(",n-1,n)

        return res        