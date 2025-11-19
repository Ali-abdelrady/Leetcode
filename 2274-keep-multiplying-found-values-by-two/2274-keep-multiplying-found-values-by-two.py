class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        def binary_search(arr, target):
            left = 0 
            right = len(arr) - 1

            while left <= right :
                mid = (left + right) // 2

                if arr[mid] == target:
                    return True
                elif arr[mid] < target:
                    left = mid + 1
                else :
                    right = mid - 1
            
            return False

        # Sort nums 
        nums.sort()

        while True :
            if not binary_search(nums, original):
                return original

            original *= 2
        
        return 0
        