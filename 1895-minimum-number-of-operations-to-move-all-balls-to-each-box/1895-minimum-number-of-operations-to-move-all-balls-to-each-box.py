class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        left_prefix = [0]*n
        right_prefix = [0]*n
        right_cnt = 0
        left_cnt = 0


        for i in range(1 , n):
            if boxes[i-1] == '1':
                left_cnt += 1
            
            left_prefix[i] += (left_prefix[i-1] + left_cnt) if left_prefix[i-1] else left_cnt
            
        for i in range(n-2 , -1 , -1):
            if boxes[i+1] == '1':
                right_cnt += 1

            right_prefix[i] += (right_prefix[i+1] + right_cnt) if right_prefix[i+1] else right_cnt

        print(boxes)
        print(left_prefix,right_prefix)
        res = []
        for i in range(n):
            res.append(left_prefix[i] + right_prefix[i])

        return res 
