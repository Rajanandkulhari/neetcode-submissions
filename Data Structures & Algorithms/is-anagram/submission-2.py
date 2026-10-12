class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        hash_s = {}

        for ch in s:
            if ch not in hash_s:
                hash_s[ch] = 1
            hash_s[ch] = hash_s[ch] + 1   

        hash_t = {}
        
        for ch in t:
            if ch not in hash_t:
                hash_t[ch] = 1
            hash_t[ch] = hash_t[ch] + 1

        if hash_s != hash_t:
            return False
        return True    