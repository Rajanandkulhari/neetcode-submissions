class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen ={}
        for i in range(len(nums)):
            num2 = nums[i]

            if num2 in seen:
                return True
            seen[nums[i]] = i
        return False    