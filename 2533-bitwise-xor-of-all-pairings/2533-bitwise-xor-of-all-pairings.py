class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)
        res = 0
        if m % 2 != 0 :
            for i in range(n):
                res ^= nums2[i]
        if n % 2 != 0 :
            for i in range(m):
                res ^= nums1[i]
        return res        