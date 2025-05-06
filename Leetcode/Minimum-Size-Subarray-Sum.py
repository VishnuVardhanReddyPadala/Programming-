class Solution:
    def minSubArrayLen(self, target, nums):
        n = len(nums)
        prefix_sums = [0] * (n + 1)

        for i in range(n):
            prefix_sums[i + 1] = prefix_sums[i] + nums[i]

        min_length = float('inf')

        for i in range(n):
            required = target + prefix_sums[i]
            left, right = i + 1, n
            while left <= right:
                mid = (left + right) // 2
                if prefix_sums[mid] >= required:
                    min_length = min(min_length, mid - i)
                    right = mid - 1
                else:
                    left = mid + 1

        return 0 if min_length == float('inf') else min_length
