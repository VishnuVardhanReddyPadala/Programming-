from sortedcontainers import SortedList

class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if t < 0 or k <= 0:
            return False
        
        sorted_list = SortedList()
        
        for i, num in enumerate(nums):
            if i > k:
                sorted_list.remove(nums[i - k - 1])
            
            pos = sorted_list.bisect_left(num - t)
            
            if pos < len(sorted_list) and sorted_list[pos] <= num + t:
                return True
            
            sorted_list.add(num)
        
        return False
