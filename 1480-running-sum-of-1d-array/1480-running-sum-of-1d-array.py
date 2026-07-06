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
        for l in range(1,len(nums)):
            nums[l]+=nums[l-1]
        return nums