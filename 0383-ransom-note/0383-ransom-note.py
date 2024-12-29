class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mp1 = {}
        mp2 = {}

        for ch in ransomNote:
            if ch in mp1:
                mp1[ch] += 1 
            else:
                mp1[ch] = 1
        for ch in magazine:
            if ch in mp2:
                mp2[ch] += 1 
            else:
                mp2[ch] = 1

        for ch,freq in mp1.items():
            if not ch in mp2 or mp2[ch] < freq:
                return False

        return True