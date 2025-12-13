class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        categories = {
            "electronics":[], 
            "grocery":[],
            "pharmacy":[], 
            "restaurant":[],
        }

        def isValidCode(code):
            return bool(re.fullmatch(r"[A-Za-z0-9_]+",code))

        for i in range(len(code)):
            if isActive[i] and businessLine[i] in categories and isValidCode(code[i]):
                categories[businessLine[i]].append(code[i])

        res = []
        for value in categories.values():
            res.extend(sorted(value))        
        
        return res