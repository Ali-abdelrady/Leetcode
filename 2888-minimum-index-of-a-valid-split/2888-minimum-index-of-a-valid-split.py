class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        # Find the dominant element using map 
        freq = Counter(nums)
        dominant_num = max(freq,key=freq.get)
        n = len(nums)
        dominant_cnt = 0 
        for i in range(n-1):
            left_size = i + 1 
            right_size =  n - i - 1
            if nums[i] == dominant_num:
                dominant_cnt += 1
            if  dominant_cnt * 2 > left_size and (freq[dominant_num] - dominant_cnt) * 2 > right_size :
                return i

        return -1 