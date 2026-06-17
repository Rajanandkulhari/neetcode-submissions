class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen =[]
        indexes=[]
        for i in nums:
            if target- i in seen:
                if nums.index(target- i) == nums.index(i):
                                    pass
                indexes.append(nums.index(target-i))
                indexes.append(nums.index(i))
            seen.append(i)
            
        return indexes