class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram ={}

        for s in strs:
            count =[0]*26
            for c in s:
               count[ord(c)-ord('a')] +=1
            if tuple(count) in anagram:
                anagram[tuple(count)].append(s)
            else:
                anagram[tuple(count)] = [s]  
        return list(anagram.values())            
                

        
                           
