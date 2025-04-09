class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # 1) Sort array
        nums.sort()
        n = len(nums)
        st = set()
        smallest_el = nums[0]
        for num in nums:
            if num != k :
                st.add(num)
        
        return len(st) if smallest_el >= k else -1
        