class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen ={}
        target = 0
        for i in range(len(nums)):
            num2 = target + nums[i]

            if num2 in seen:
                return True
            seen[nums[i]] = i
        return False    