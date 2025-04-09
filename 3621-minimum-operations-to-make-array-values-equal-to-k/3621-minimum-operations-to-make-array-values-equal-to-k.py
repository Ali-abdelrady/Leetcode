class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        n = len(nums)
        st = set()
        for num in nums:
            st.add(num)
        
        if min(st) < k :
            return -1 

        return len(st) - 1 if k in st else len(st)
        