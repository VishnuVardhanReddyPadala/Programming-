class Solution:
    def rob(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        def rob_linear(houses):
            prev = curr = 0
            for amount in houses:
                prev, curr = curr, max(curr, prev + amount)
            return curr

        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))
