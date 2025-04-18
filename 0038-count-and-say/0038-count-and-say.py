class Solution:
    def countAndSay(self, n: int) -> str:
        seq = "1"
        for i in range(n-1):
            newSeq = ""
            cnt = 1 
            for i in range(len(seq)):
                if i + 1 < len(seq) and seq[i] == seq[i+1]:
                    cnt += 1
                else:
                    newSeq += str(cnt) + seq[i]
                    cnt = 1
            seq = newSeq
        return seq

            