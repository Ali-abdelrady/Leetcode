class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left_sub = []
        right_sub = []
        pivot_freq = 0

        for num in nums:
            if num == pivot:
                pivot_freq += 1
            elif num < pivot:
                left_sub.append(num)
            else:
                right_sub.append(num)

        return (left_sub + [pivot]*pivot_freq + right_sub)        