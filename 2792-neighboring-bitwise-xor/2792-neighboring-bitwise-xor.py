class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        bit = 0 
        for num in derived:
            if num == 1:
                bit = 1 - bit

        return bit == 0