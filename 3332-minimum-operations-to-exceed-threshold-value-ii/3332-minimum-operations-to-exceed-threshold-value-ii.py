from queue import PriorityQueue
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        pq = PriorityQueue()

        for num in nums :
            pq.put((0,num))


        op = 0
        while not pq.empty():
            _ , fstEl = pq.get()
            
            if fstEl >= k:
                return op

            _ , secEl = pq.get()
            res = (fstEl * 2) + secEl
            pq.put((0,res))
            op += 1        