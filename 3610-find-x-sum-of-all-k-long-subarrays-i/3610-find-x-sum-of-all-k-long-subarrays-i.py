class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        def x_sum(nums,x):

            # Count occurence
            mp = Counter(nums)

            # Check if len of map < x
            if len(mp) < x:
                return sum(nums)
            
            # Extract key-value in list 
            arr = []
            for key,value in mp.items():
                arr.append((value,key))

            # Sort list by values
            arr.sort(reverse=True)

            # Select the largest x num and calc thier sum 
            return sum(k * v for v,k in arr[:x])
        n = len(nums)
        ans = []
        ans_len = n-k+1
        for i in range(ans_len):
            ans.append(x_sum(nums[i:i+k],x))

        return ans