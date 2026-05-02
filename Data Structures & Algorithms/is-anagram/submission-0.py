class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        result1 = "".join(sorted(s))  
        result2 = "".join(sorted(t))  
        if result1 == result2:
            return True
        return False