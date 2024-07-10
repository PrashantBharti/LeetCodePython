class Solution:
    def nextPermutation(self, nums):
        if not nums or len(nums) < 2:
            return
        
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
            
        if i < 0:
            nums.sort()
            return
            
        j = len(nums) - 1
        while j > i and nums[j] <= nums[i]:
            j -= 1
            
        nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1:] = sorted(nums[i + 1:])