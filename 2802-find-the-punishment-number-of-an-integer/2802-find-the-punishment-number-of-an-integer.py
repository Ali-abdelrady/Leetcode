class Solution:
    def punishmentNumber(self, n: int) -> int:
        def backtrack(num,cur_sum,i,target):
            if i == len(num):
                return cur_sum == target
            for j in range(i + 1,len(num) + 1):
                if backtrack(num , cur_sum + int(num[i:j]) , j,target):
                    return True
                
            return False


        res = 0
        for num in range(1,n+1):
            square_num = pow(num,2)
            if backtrack(str(square_num) , 0 , 0 , num):
                res += square_num

        return res
        