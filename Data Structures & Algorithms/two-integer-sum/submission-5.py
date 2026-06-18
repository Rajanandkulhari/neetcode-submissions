class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen =[]
        for i in range(len(nums)):
            j = target - nums[i]
            if j in seen:
                index =[seen.index(j),i]
                break
            seen.append(nums[i])
        return index


        