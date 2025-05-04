class Solution:
    def rob(self, nums):
        prev_max = 0
        curr_max = 0
        for num in nums:
            temp = curr_max
            curr_max = max(curr_max, prev_max + num)
            prev_max = temp
        return curr_max
