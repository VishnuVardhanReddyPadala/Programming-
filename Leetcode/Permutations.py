class Solution:
    def permute(self, nums):
        res = []

        def backtrack(start=0):
            if start == len(nums):
                res.append(nums[:])
                return
            
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]  # Swap
                backtrack(start + 1)  # Recurse
                nums[start], nums[i] = nums[i], nums[start]  # Undo swap (backtrack)

        backtrack()
        return res
