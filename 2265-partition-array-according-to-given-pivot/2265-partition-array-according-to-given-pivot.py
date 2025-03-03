class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left_sub = []
        right_sub = []
        mid_sub = []

        for num in nums:
            if num == pivot:
                mid_sub.append(num)
            elif num < pivot:
                left_sub.append(num)
            else:
                right_sub.append(num)

        return (left_sub + mid_sub + right_sub)        