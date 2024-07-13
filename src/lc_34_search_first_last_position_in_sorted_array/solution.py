class Solution:
    def searchRange(self, nums, target):
        if not nums:
            return [-1, -1]
        
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                i = j = mid
                while i > 0 and nums[i - 1] == target:
                    i -= 1
                while j < len(nums) - 1 and nums[j + 1] == target:
                    j += 1
                return [i, j]
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
                
        return [-1, -1]