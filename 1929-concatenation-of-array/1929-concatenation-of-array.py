class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a=[]
        for i in range(0,(len(nums)*2)):
            if i<len(nums):
                a.append(nums[i])
            else:
                a.append(nums[i-len(nums)])
        return a