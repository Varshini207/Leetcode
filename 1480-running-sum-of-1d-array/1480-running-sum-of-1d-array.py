class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        '''a=[]
        s=0
        for i in range(len(nums)):
            s+=nums[i]
            a.append(s)
        return a'''
        l=1
        while l<len(nums):
            nums[l]=nums[l]+nums[l-1]
            l+=1
        return nums