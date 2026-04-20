class Solution(object):
    def isMonotonic(self, nums):
        a=True
        d=True
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                d=False
            elif nums[i]<nums[i+1]:
                a=False
        return a or d