class Solution:
    def sortColors(self, nums: List[int]) -> None:
        freq = Counter(nums)
        zero = [0]*freq[0]
        one = [1]*freq[1]
        two = [2]*freq[2]
        nums[:] = zero + one + two
        