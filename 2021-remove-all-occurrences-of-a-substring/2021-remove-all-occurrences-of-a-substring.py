class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        st = ""
        for ch in s:
            st += ch
            if  ch == part[-1] and st[len(st)-len(part):] == part:
                st = st[:len(st)-len(part)]        

        return st
        