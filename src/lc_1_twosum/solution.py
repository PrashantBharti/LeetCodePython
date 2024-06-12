class Solution:
    def __init__(self):
        pass
    
    def twoSum(self, nums, target):
        map = {}
        
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in map:
                return [map[diff], idx]
            else:
                map[num] = idx
                
        raise ValueError("No two sum solution")
