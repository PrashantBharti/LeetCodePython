import math
from collections import namedtuple

class Solution:
    Cut = namedtuple('cut', ['l1', 'r1', 'l2', 'r2'])
    
    def __init__(self):
        pass
    
    def findMedianSortedArrays(self, nums1, nums2):
        if not nums1:
            return self.get_median(nums2)
        elif not nums2:
            return self.get_median(nums1)
        
        merged_size = len(nums1) + len(nums2)
        low_nums1 = 0
        high_nums1 = len(nums1) - 1
        
        cut1 = -1
        cut2 = -1
        
        while low_nums1 <= high_nums1:
            cut1 = low_nums1 + (high_nums1 - low_nums1) // 2
            cut2_size = (merged_size // 2) - cut1 - 1
            if cut2_size < 0:
                high_nums1 = cut1 - 1
                continue
            elif cut2_size > len(nums2):
                low_nums1 = cut1 + 1
                continue
            else:
                cut2 = cut2_size - 1

            cut = self.get_cut_values(nums1, nums2, cut1, cut2)
            if cut.l1 > cut.r2:
                high_nums1 = cut1 - 1
                if high_nums1 < low_nums1:
                    cut1 = -1
                    cut2 = (merged_size // 2) - 1
            elif cut.l2 > cut.r1:
                low_nums1 = cut1 + 1
            else:
                break
        
        cut = self.get_cut_values(nums1, nums2, cut1, cut2)
        if merged_size % 2 == 0:
            return (max(cut.l1, cut.l2) + min(cut.r1, cut.r2)) / 2
        else:
            return min(cut.r1, cut.r2)
    
    def get_cut_values(self, nums1, nums2, cut1, cut2):
        l1 = self.get_left(nums1, cut1)
        r1 = self.get_right(nums1, cut1)
        l2 = self.get_left(nums2, cut2)
        r2 = self.get_right(nums2, cut2)

        return self.Cut(l1, r1, l2, r2)
    
    def get_left(self, nums, cut):
        if cut < 0:
            return -math.inf
        else:
            return nums[cut]
        
    def get_right(self, nums, cut):
        if cut == len(nums) - 1:
            return math.inf
        else:
            return nums[cut + 1]
    
    def get_median(self, nums):
        if not nums:
            return None
        
        size = len(nums)
        mid = (size - 1) // 2
        if size % 2 == 0:
            return (nums[mid] + nums[mid + 1]) / 2
        else:
            return nums[mid]
