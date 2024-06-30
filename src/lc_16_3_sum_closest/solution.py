class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        closest_sum = float('inf')
        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if abs(target - sum) < abs(target - closest_sum):
                    closest_sum = sum
                    
                if sum < target:
                    l += 1
                elif sum > target:
                    r -= 1
                else:
                    return target
                
        return closest_sum