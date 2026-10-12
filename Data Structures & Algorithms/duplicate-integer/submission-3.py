class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
      hash_arr = {}

      for num in nums:
        if hash_arr.get(num,0)!= 0:
            return True
        hash_arr[num] = hash_arr.get(num,0)+1
      return False  