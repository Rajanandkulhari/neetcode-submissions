class Solution:
    def check(self, nums: List[int]) -> bool:
       new1 = [nums[0]]
       
       index = 0
       for i in range(1,len(nums)):
        
          if nums[i-1]<=nums[i]:
            new1.append(nums[i])
          else:
            index = i
            break
       new2 = [nums[index]]
       if index!=0:
        for i in range(index+1,len(nums)):
            
            if nums[i-1]<=nums[i]:
                new2.append(nums[i])
            else :
                return False

       results = new2+new1
        
       for  i in range(1,len(results)):
         if results[i-1]>results[i]:
            print(results)
            return False
       return True
