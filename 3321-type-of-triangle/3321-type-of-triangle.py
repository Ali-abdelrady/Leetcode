class Solution:
    def triangleType(self, nums: List[int]) -> str:
        diff_sides= Counter(nums)
        if len(diff_sides) == 1:
            return "equilateral"

        # Check for side if it's valid for triangle
        if (nums[0] + nums[1] > nums[2]) and  (nums[0] + nums[2] > nums[1]) and (nums[1] + nums[2] > nums[0]):
            return "isosceles" if len(diff_sides) == 2 else "scalene" 

        return "none"
