class Solution:
    def findKthLargest(self, nums, k):
        nums.sort(reverse=True)
        return nums[k - 1]

solution = Solution()
param_1 = [3, 2, 1, 5, 6, 4]
param_2 = 2

solution = Solution()
ret = solution.findKthLargest(param_1, param_2)
print(ret)